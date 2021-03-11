'''

** Bangla Text preprocessor **

Punctuation remove: remove all type of punctuation and replace punctuation with a SPACE
dust_removal : remove all kind of character(including English character, punctuation) without Bangla character Aভাই23 = ভাই
stopword_remove: remove stopword from text
word_normalize: similar Bangla vowel defines same character : অসহনীয় ভারী বর্ষণে : অসহনিয় ভারি বর্ষণে
bangla_to_english_Conversion: Bangla to English word equivalent word conversion : রাজধানী : rajdhani
bnCompare: compare function
isBangla: is Bangla character exist in this word?
bn_word_sort_en_sys: Sort bangla word according to English alphabet (a,b,c,......)
bn_word_sort_bn_sys: Sort bangla word according to Bangla alphabet(অ,.....)
is_number: is bangla number?

'''


import re
import functools
from sbnltk import sbnltk_default
from sbnltk.Downloader import downloader

class StaticArray:
    bn2en={'0985':'a','0986':'a','0987':'i','0988':'i',
           '0989':'u','098A':'u','098B':'r','09E0':'r',
           '098C':'l','09E1':'l','098F':'e','0990':'oi',
           '0993':'o','0994':'ou',
           '0995':'k','0996':'kh','0997':'g','0998':'gh',
           '0999':'ng','099A':'c','099B':'ch','099C':'j',
           '099D':'jh','099E':'ny','099F':'tt', '09A0':'tth',
           '09A1':'dd','09DC':'rr','09A2':'ddh','09DD':'rh',
           '09A3':'nn','09A4':'t','09A5':'th','09A6':'d',
           '09A7':'dh','09A8':'n','09AA':'p','09AB':'ph',
           '09AC':'b','09AD':'bh','09AE':'m','09AF':'y',
           '09DF':'yy','09B0':'r','09B2':'l','09B6':'sh',
           '09B7':'ss','09B8':'s','09B9':'h','09CE':'t',
           '09BE':'a','09BF':'i','09C0':'i','09C1':'u',
           '09C2':'u','09C3':'r','09C4':'r','09C7':'e',
           '09C8':'oi', '09CB':'o','09CC':'au',
           '09CD':'','09D7':'','09E6':'0',
           '09E7':'1','09E8':'2','09E9':'3','09EA':'4',
           '09EB':'5','09EC':'6','09ED':'7','09EE':'8',
           '09EF':'9',
           '09BC':'','0982':'n','0983':'','0981':''
           }
    bn2enNum={
        '09E6': '0',
        '09E7': '1', '09E8': '2', '09E9': '3', '09EA': '4',
        '09EB': '5', '09EC': '6', '09ED': '7', '09EE': '8',
        '09EF': '9'
    }
    bn2enPunc={
        '09BE': 'a', '09BF': 'i', '09C0': 'i', '09C1': 'u',
        '09C2': 'u', '09C3': 'r', '09C4': 'r', '09C7': 'e',
        '09C8': 'ai', '09CB': 'o', '09CC': 'au','09B0':'ra'
    }
    bn2enSuffix={
        '09BE': 'a', '09B0':'ra','09CB': 'o','0993':'o','09C7': 'e'
    }
    bn_norm={
        '09C0':'\u09bf','09C2':'\u09c1','09C4':'\u09c3','09A3':'\u09a8','0988':'\u0987','098A':'\u0989'
    }

    bn_serial={
        '0985': 0, '0986': 1, '09BE': 2, '0987': 3, '09BF': 4,'0988': 5, '09C0': 6,
        '0989': 7, '09C1': 8, '098A': 9, '09C2': 10,'098B': 11,'09C3': 12, '09E0': 13,'09C4': 14,
        '098C': 15, '09E1': 16, '098F': 17,  '09C7': 18, '0990': 19,'09C8': 20,
        '0993': 21, '09CB': 22, '0994': 23, '09CC': 24,
        '0995': 25, '0996': 26, '0997': 27, '0998': 28,
        '0999': 29, '099A': 30, '099B': 31, '099C': 32,
        '099D': 33, '099E': 34, '099F': 35, '09A0': 36,
        '09A1': 37, '09DC': 38, '09A2': 39, '09DD': 40,
        '09A3': 41, '09A4': 42, '09A5': 43, '09A6': 44,
        '09A7': 45, '09A8': 46, '09AA': 47, '09AB': 48,
        '09AC': 49, '09AD': 50, '09AE': 51, '09AF': 52,
        '09DF': 53, '09B0': 54, '09B2': 55, '09B6': 56,
        '09B7': 57, '09B8': 58, '09B9': 59, '09CE': 60,
        '09E6': 61,
        '09E7': 62, '09E8': 63, '09E9': 64, '09EA': 65,
        '09EB': 66, '09EC': 67, '09ED': 68, '09EE': 69,
        '09EF': 70,
        '09CD': 71, '09D7': 72,
        '09BC': 73, '0982': 74, '0983': 75, '0981': 76
    }

class preprocessor:

    __dl=downloader()
    __word_list = {}
    __stopwords=[]
    def __init__(self):
        self.__dl.download('bangla_word_list', sbnltk_default.sbnltk_root_path+'dataset/')
        self.__dl.download('stopword_list', sbnltk_default.sbnltk_root_path+'dataset/')
        for line in open(sbnltk_default.sbnltk_root_path+'dataset/bangla_word_list.txt', 'r'):
            line = line.rstrip('\n')
            self.__word_list[line] = 1
        model_path = sbnltk_default.sbnltk_root_path+"dataset/stopword_list.txt"
        for i in open(model_path, "r"):
            i = i.rstrip("\n")
            self.__stopwords.append(i)

    def punctuation_remove(self,text):
        try:
            whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
            bangla_fullstop = u"\u0964"
            punctSeq = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
            punc = u"[(),$%^&*+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
            text = whitespace.sub(" ", text).strip()
            text = re.sub(punctSeq, " ", text)
            text = re.sub(bangla_fullstop, " ", text)
            text = re.sub(punc, " ", text)
            text = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', ' ', text)
            text=text.replace("\\", " ")
            return text
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 201: Error in Removing punctuation!! {sbnltk_default.bcolors.ENDC}")
            return text


    def dust_removal(self,word):

        try:
            s=""
            for c in word:
                g = c.encode("unicode_escape")
                g = g.upper()
                g = g[2:]
                g = g.decode('utf-8')
                if g in StaticArray.bn2en:
                    s+=c
            if len(s)==0:
                return word
            return s
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 202: Error in Removing dust!! {sbnltk_default.bcolors.ENDC}")
            return word

    def dust_removal_sent(self,sentence):
        words=sentence.split()
        temp=[]
        for i in words:
            temp.append(self.dust_removal(i))
        temp=' '.join(temp)
        return  temp
    def stopword_remove(self,text):
        try:
            querywords = text.split()
            resultwords = [word for word in querywords if word not in self.__stopwords]
            result = ' '.join(resultwords)
            return result
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 203: Error in Removing stop word!! {sbnltk_default.bcolors.ENDC}")
            return text

    def word_normalize(self,word):
        try:
            s = ""
            for c in word:
                g = c.encode("unicode_escape")
                g = g.upper()
                g = g[2:]
                g = g.decode('utf-8')
                if g in StaticArray.bn_norm:
                    g = StaticArray.bn_norm[g].encode().decode('utf-8')
                    s+=g
                    continue
                s+=c
            return s
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 204: Error in word normalization!! {sbnltk_default.bcolors.ENDC}")
            return word


    def bangla_to_english_Conversion(self,word):
        try:
            s=""
            for c in word:
                g=c.encode("unicode_escape")
                g=g.upper()
                g=g[2:]
                g=g.decode('utf-8')
                if g in StaticArray.bn2enPunc:
                    if len(s)>0 and s[-1]=='a':
                        s=s[:-1]
                    s+=StaticArray.bn2enPunc[g]
                    continue
                if g in StaticArray.bn2en:
                    s+=StaticArray.bn2en[g]
            return s
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 205: Error in Bangla to English Conversion!! {sbnltk_default.bcolors.ENDC}")
            return word


    def __bnCompare(self,item1,item2):
        g1=self.bangla_to_english_Conversion(item1)
        g2=self.bangla_to_english_Conversion(item2)
        return (g1 > g2) - (g1 < g2)

    def isBanglaWord(self,word):
        if word in self.__word_list:
            return True
        return False

    def isBangla(self,word):
        for c in word:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn2en:
                return True
        return False

    def bn_word_sort_en_sys(self,vec):
        try:
            temp_vec=[]
            for i in vec:
                if self.isBangla(i):
                  i=self.dust_removal(i)
                  temp_vec.append(self.punctuation_remove(i).replace(' ',''))
            vec=list(set(temp_vec))
            vec=sorted(vec,key=functools.cmp_to_key(self.__bnCompare))
            return vec
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 206: Error in Sort bangla words according English alphabet!! {sbnltk_default.bcolors.ENDC}")
            return vec

    def __bnCompare2(self,item1,item2):
        ln=min(len(item1),len(item2))
        for i in range(ln):
            if item1[i]==item2[i]:
                continue
            g1 = item1[i].encode("unicode_escape")
            g1 = g1.upper()
            g1 = g1[2:]
            g1 = g1.decode('utf-8')
            g1=StaticArray.bn_serial[g1]
            g2 = item2[i].encode("unicode_escape")
            g2 = g2.upper()
            g2 = g2[2:]
            g2 = g2.decode('utf-8')
            g2=StaticArray.bn_serial[g2]
            return (g1>g2) -(g1<g2)
        return (len(item1)>len(item2))-(len(item1)<len(item2))
    def bn_word_sort_bn_sys(self,vec):
        try:
            temp_vec = []
            for i in vec:
                if self.isBangla(i):
                    i = self.dust_removal(i)
                    temp_vec.append(self.punctuation_remove(i).replace(' ', ''))
            vec = list(set(temp_vec))
            vec = sorted(vec, key=functools.cmp_to_key(self.__bnCompare2))
            return vec
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 207: Error in Sort Bangla words according Bangla alphabet!! {sbnltk_default.bcolors.ENDC}")
            return vec

    def is_number(self,word):
        for c in word:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g in StaticArray.bn2enNum:
                return True
        return False
    def extra_space_remove(self,sent):
        while len(sent)>0 and sent[0]==' ':
            sent=sent[1:]
        temp=''
        for i in sent:
            if len(temp)>0 and temp[-1]==' ' and i==' ':
                continue
            temp+=i
        return temp





