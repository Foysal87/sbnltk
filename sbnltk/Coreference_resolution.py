import re
from sbnltk.Ner_bert import Bert_Multilingual_Uncased_Ner
from sbnltk.Tokenizer import wordTokenizer,sentenceTokenizer

class plural:
    __suffix=['গুলো','গুলোর','েরগুলো','েরগুলোর']
    def is_plural(self,word):
        suf_arr = []
        for wd in self.__suffix:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        if len(suf_arr)>0:
            return True
        return False

class static:
    __suffix=['ই', 'ও', 'কে', 'তে', 'রা', 'য়', 'য়ে','ের', 'ার', 'েন','ে','টা', 'টার', 'গুলো', 'গুলোর', 'েরগুলো', 'েরগুলোর'
              'যোগ্য','কেই','েও','সহ','রা','ই','কে','র','কি','েই','গুলো',
              'তে','েতে','ি','য়','টি', 'টির']
    __loc=['স্থান','জায়গা','অবস্থান','স্থানটি','শহর','রাজধানী','নগর','এলাকা','অঞ্চল','বন্দর','প্রদেশ','গ্রাম','দেশ','রাষ্ট্র']
    __org=['সংগঠন','প্রতিষ্ঠান','সংস্থা','সংঘ','দল','সম্প্রদায়','এনজিও','গোষ্ঠী','সমাজ','ফোরাম']
    __per=['ব্যক্তি','মানুষ','লোক','নারী','মহিলা','ছেলে']
    __date=['তারিখ','দিন','সময়','বছর','মাস','সপ্তাহ','দিন','শতক']
    def isLoc(self,word):
        suf_arr = []
        for wd in self.__suffix:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        for i in suf_arr:
            ind = len(word) - len(i)
            new_word = word[0:ind]
            if new_word in self.__loc:
                return True
        return False
    def isOrg(self,word):
        suf_arr = []
        for wd in self.__suffix:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        for i in suf_arr:
            ind = len(word) - len(i)
            new_word = word[0:ind]
            if new_word in self.__org:
                return True
        return False
    def isPer(self,word):
        suf_arr = []
        for wd in self.__suffix:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        for i in suf_arr:
            ind = len(word) - len(i)
            new_word = word[0:ind]
            if new_word in self.__per:
                return True
        return False
    def isDate(self,word):
        suf_arr = []
        for wd in self.__suffix:
            if re.search('.*' + wd + '$', word):
                suf_arr.append(wd)
        for i in suf_arr:
            ind = len(word) - len(i)
            new_word = word[0:ind]
            if new_word in self.__date:
                return True
        return False

class Pronoun:
    __person_singular=['আমি','তুই','তুমি','আপনি','ইনি','উনি','সে','তিনি']
    __person_singular_f=['ও','এ']
    __object_singular=['এটি','এটা','ওটি','ওটা','সেটি','সেটা']
    __person_objective_singular=['আমাকে','তোকে','তোমাকে','আপনাকে','একে','এঁকে','তাকে','তাঁকে','ওঁকে','ওকে']
    __person_possessive_singular=['আমার','তোর','তোমার','আপনার','তার','তাঁর']
    __object_possessive_singular=['এটির','এটার','ওটির','ওটার','সেটির','সেটার']
    __person_plural=['আমরা','তোরা','তোমরা','আপনারা','এরা','এঁরা','ওরা','ওঁরা','তারা','তাঁরা']
    __object_plural=['এগুলো','ওগুলো','সেগুলো']
    __person_objective_plural=['আমাদেরকে','তোদেরকে','তোমাদেরকে','আপনাদেরকে','এদেরকে','এঁদেরকে','ওদেরকে','ওঁদেরকে','তাদেরকে','তাঁদেরকে']
    __object_objective_plural=['এগুলো','ওগুলো','সেগুলো']
    __person_possessive_plural=['আমাদের','তোদের','তোমাদের','আপনাদের','এদের','এঁদের','ওদের','ওঁদের','তাদের','তাঁদের']
    __object_possessive_plural=['এগুলোর','ওগুলোর','সেগুলোর']
    __own_singular=['নিজেকে','নিজে','নিজেই','নিজের','নিজেরই','নিজেরও']
    __own_plural=['নিজেদের','নিজেরা','নিজেরাই']
    __all=['এই']
    def isPronoun(self,word):
        if word in self.__person_singular:
            return (True,'PS')
        if word in self.__object_singular:
            return (True,'OS')
        if word in self.__person_objective_singular:
            return (True,'POS')
        if word in self.__person_possessive_singular:
            return (True,'PPS')
        if word in self.__object_possessive_singular:
            return (True,'OPS')
        if word in self.__person_plural:
            return (True,'PP')
        if word in self.__object_plural:
            return (True,'OP')
        if word in self.__person_objective_plural:
            return (True,'POP')
        if word in self.__object_objective_plural:
            return (True,'OOP')
        if word in self.__person_possessive_plural:
            return (True,'PPP')
        if word in self.__object_possessive_plural:
            return (True,'OPP')
        if word in self.__own_singular:
            return (True, 'OWS')
        if word in self.__own_plural:
            return (True,'OWP')
        if word in self.__all:
            return (True,'A')
        return (False,'O')

class coreference_resolution:
    __nerT=None
    __wordT=None
    __sentT=None
    __nerS=None
    __pro = Pronoun()
    __plu = plural()
    __sta = static()
    __last_person_singular = []
    __last_person_plural = []
    __last_object_singular = []
    __last_object_plural = []
    __last_loc_singular = []
    __last_date_singular = []
    __last_org_singular = []
    __last_loc_plural = []
    __last_date_plural = []
    __last_org_plural = []
    def __init__(self):
        self.__nerT=Bert_Multilingual_Uncased_Ner()
        self.__wordT=wordTokenizer()
        self.__sentT=sentenceTokenizer()
    def __cluster(self,vec):
        temp=[]
        lst=""
        ent=[]
        k=1
        for i in vec:
            for j in i:
                if(i[j][0]=='S'):
                    if len(ent)>0:
                        l=len(ent)
                        ent=' '.join(ent)
                        temp.append((k-l,k-1,ent,lst))
                        ent=[]
                        lst=""
                    temp.append((k,k,j,i[j][2:]))
                elif (i[j][0]=='B'):
                    if len(ent)>0:
                        l = len(ent)
                        ent=' '.join(ent)
                        temp.append((k-l,k-1,ent,lst))
                        ent=[]
                        lst=""
                    else:
                        ent.append(j)
                        lst=i[j][2:]
                elif (i[j][0]=='I' or i[j][0]=='E'):
                    tm=i[j][2:]
                    if tm!=lst and lst!="":
                        l = len(ent)
                        ent = ' '.join(ent)
                        temp.append((k-l, k-1,ent, lst))
                        ent = []
                        lst = ""
                    else:
                        ent.append(j)
                        lst = i[j][2:]
                else:
                    if len(ent)>0:
                        l = len(ent)
                        ent=' '.join(ent)
                        temp.append((k-l,k-1,ent,lst))
                        ent=[]
                        lst=""
                    if j=="ও":
                        temp.append((k,k,j, "CON"))
            k+=1
        if len(ent) > 0:
            l = len(ent)
            ent = ' '.join(ent)
            temp.append((k - l, k - 1, ent, lst))
            ent = []
            lst = ""
        return temp

    def __get_entity(self,sentences):
        temp2=self.__nerT.tag(sentences)
        entity=[]
        mp=[]
        mp2=[]
        for i in range(len(temp2)):
            z=self.__cluster(temp2[i])
            z=list(set(z))
            entity.append(z)
            tmp={}
            tmp2={}
            for j in range(len(z)):
                 k=z[j]
                 tmp[(int)(k[0])]=(k[2],k[3])
                 tmp2[(int)(k[1])]=(k[2],k[3])
            mp.append(tmp)
            mp2.append(tmp2)
        return mp,mp2

    def __set_ent(self,word1,ent,ind,word_i,word2=None):
        if ent=='PER':
            if word2==None:
                self.__last_person_singular.append((word1,ind,word_i))
            elif self.__plu.is_plural(word1) and word2==None:
                self.__last_person_plural.append((word1, ind,word_i))
            else:
                self.__last_person_singular.append((word1,ind,word_i))
                self.__last_person_singular.append((word2,ind,word_i))
                self.__last_person_plural.append((word1+' ও '+word2,ind,word_i))
        if ent=='OBJ':
            if word2==None:
                if self.__plu.is_plural(word1):
                    self.__last_object_plural.append((word1, ind,word_i))
                else:
                    self.__last_object_singular.append((word1,ind,word_i))
            else:
                if self.__plu.is_plural(word1)==False and self.__plu.is_plural(word2)==False:
                    self.__last_object_singular.append((word1,ind,word_i))
                    self.__last_object_singular.append((word2,ind,word_i))
                    self.__last_object_plural.append((word1 + ' ও ' + word2, ind,word_i))
                else:
                    self.__last_object_plural.append((word1, ind,word_i))
                    self.__last_object_plural.append((word2, ind,word_i))
        if ent=='LOC':
            if word2==None:
                self.__last_loc_singular.append((word1,ind,word_i))
            elif self.__plu.is_plural(word1) and word2==None:
                self.__last_loc_plural.append((word1, ind,word_i))
            else:
                self.__last_loc_singular.append((word1,ind,word_i))
                self.__last_loc_singular.append((word2,ind,word_i))
                self.__last_loc_plural.append((word1+' ও '+word2,ind,word_i))
        if ent=='ORG':
            if word2==None:
                self.__last_org_singular.append((word1,ind,word_i))
            elif self.__plu.is_plural(word1) and word2==None:
                self.__last_org_plural.append((word1, ind,word_i))
            else:
                self.__last_org_singular.append((word1,ind,word_i))
                self.__last_org_singular.append((word2,ind,word_i))
                self.__last_org_plural.append((word1+' ও '+word2,ind,word_i))
        if ent=='DATE':
            if word2==None:
                self.__last_date_singular.append((word1,ind,word_i))
            elif self.__plu.is_plural(word1) and word2==None:
                self.__last_date_plural.append((word1, ind,word_i))
            else:
                self.__last_date_singular.append((word1,ind,word_i))
                self.__last_date_singular.append((word2,ind,word_i))
                self.__last_date_plural.append((word1+' ও '+word2,ind,word_i))

    # For renew the entity, After resolving i push it again in entity list
    def __set_ent_renew(self,word,type,i,word_i):
        if (type=='PS'):
            self.__last_person_singular.append((word,i,word_i))
        elif type=='PP':
            self.__last_person_plural.append((word, i,word_i))
        elif type=='OS':
            self.__last_object_singular.append((word, i,word_i))
        elif type=='OP':
            self.__last_object_plural.append((word, i,word_i))
        elif type=='LOCS':
            self.__last_loc_singular.append((word, i,word_i))
        elif type=='LOCP':
            self.__last_loc_plural.append((word, i,word_i))
        elif type=='ORGS':
            self.__last_org_singular.append((word, i,word_i))
        elif type=='ORGP':
            self.__last_org_plural.append((word, i,word_i))
        elif type=='DATES':
            self.__last_date_singular.append((word, i,word_i))
        elif type=='DATEP':
            self.__last_date_plural.append((word, i,word_i))
    def __is_last_ch_vowel(self,word):
        tag=['া','ি','ী','ু','ূ','ৃ','ে','ৈ','ো','ৌ','আ','ই','ঈ','উ','ঊ','এ','ঐ','ও','ঔ']
        if len(word)>0 and word[-1] in tag:
            return True
        return False


    # main resolve program
    def __single_resolve(self,type,i,word,word_i):
        if type == 'PS' and len(self.__last_person_singular) > 0:
            ind = len(self.__last_person_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1:
                    flg = self.__last_person_singular[ind][1]
                    flg2= self.__last_person_singular[ind][2]
                    temp_ref = self.__last_person_singular[ind][0]
                elif flg != -1 and self.__last_person_singular[ind][1] == flg:
                    flg = self.__last_person_singular[ind][1]
                    flg2 = self.__last_person_singular[ind][2]
                    temp_ref = self.__last_person_singular[ind][0]
                ind -= 1
            if flg == -1:
                self.__set_ent_renew(self.__last_person_singular[-1][0],'PS',i,word_i)
                return [self.__last_person_singular[-2][1]],[self.__last_person_singular[-2][2]],self.__last_person_singular[-1][0]
            else:
                self.__set_ent_renew(temp_ref, 'PS', i,word_i)
                return [flg],[flg2],temp_ref
        elif type == 'POS' and len(self.__last_person_singular) > 0:
            ind = len(self.__last_person_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_person_singular[ind][1] != i:
                    flg = self.__last_person_singular[ind][1]
                    flg2=self.__last_person_singular[ind][2]
                    temp_ref = self.__last_person_singular[ind][0]
                ind -= 1
            if flg == -1:
                wd = self.__last_person_singular[-1][0]
                self.__set_ent_renew(wd, 'PS', i,word_i)
                if len(wd) >= 2 and wd[len(wd) - 2:] == 'কে':
                    pass
                else:
                    wd += 'কে'
                return [self.__last_person_singular[-2][1]],[self.__last_person_singular[-2][2]],wd
            else:
                wd = temp_ref
                if len(wd) >= 2 and wd[len(wd) - 2:] == 'কে':
                    pass
                else:
                    wd += 'কে'
                self.__set_ent_renew(temp_ref, 'PS', i,word_i)
                return [flg],[flg2],wd
        elif type == 'PPS' and len(self.__last_person_singular) > 0:
            ind = len(self.__last_person_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1:
                    flg = self.__last_person_singular[ind][1]
                    flg2=self.__last_person_singular[ind][2]
                    temp_ref = self.__last_person_singular[ind][0]
                elif flg != -1 and self.__last_person_singular[ind][1] == flg:
                    flg = self.__last_person_singular[ind][1]
                    flg2 = self.__last_person_singular[ind][2]
                    temp_ref = self.__last_person_singular[ind][0]
                ind -= 1
            if flg == -1:
                wd = self.__last_person_singular[-1][0]
                self.__set_ent_renew(wd, 'PS', i,word_i)
                if self.__is_last_ch_vowel(wd):
                    wd += 'র'
                else:
                    wd += 'ের'
                return [self.__last_person_singular[-2][1]],[self.__last_person_singular[-2][2]],wd
            else:
                wd = temp_ref
                if self.__is_last_ch_vowel(wd):
                    wd += 'র'
                else:
                    wd += 'ের'
                self.__set_ent_renew(temp_ref, 'PS', i,word_i)
                return [flg],[flg2],wd



        elif type == 'OS' and len(self.__last_object_singular) > 0:
            ind = len(self.__last_object_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1:
                    flg = self.__last_object_singular[ind][1]
                    flg2=self.__last_object_singular[ind][2]
                    temp_ref = self.__last_object_singular[ind][0]
                elif flg != -1 and self.__last_object_singular[ind][1] == flg:
                    flg = self.__last_object_singular[ind][1]
                    flg2 = self.__last_object_singular[ind][2]
                    temp_ref = self.__last_object_singular[ind][0]
                ind -= 1
            if flg == -1:
                wd = self.__last_object_singular[-1][0]
                self.__set_ent_renew(wd, 'OS', i,word_i)
                return [self.__last_object_singular[-2][1]],[self.__last_object_singular[-2][2]],wd
            else:
                wd = temp_ref
                self.__set_ent_renew(temp_ref, 'OS', i,word_i)
                return [flg],[flg2],wd
        elif type == 'OOS' and len(self.__last_object_singular) > 0:
            ind = len(self.__last_object_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_object_singular[ind][1] != i:
                    flg = self.__last_object_singular[ind][1]
                    flg2=self.__last_object_singular[ind][2]
                    temp_ref = self.__last_object_singular[ind][0]
                ind -= 1
            if flg == -1:
                wd = self.__last_object_singular[-1][0]
                self.__set_ent_renew(wd, 'OS', i,word_i)
                if len(wd) >= 2 and wd[len(wd) - 2:] == 'কে':
                    pass
                else:
                    wd += 'কে'
                return [self.__last_object_singular[-2][1]],[self.__last_object_singular[-2][2]],wd
            else:
                wd = temp_ref
                if len(wd) >= 2 and wd[len(wd) - 2:] == 'কে':
                    pass
                else:
                    wd += 'কে'
                self.__set_ent_renew(temp_ref, 'OS', i,word_i)
                return [flg],[flg2],wd
        elif type == 'OPS' and len(self.__last_object_singular) > 0:
            ind = len(self.__last_object_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1:
                    flg = self.__last_object_singular[ind][1]
                    flg2= self.__last_object_singular[ind][2]
                    temp_ref = self.__last_object_singular[ind][0]
                elif flg != -1 and self.__last_object_singular[ind][1] == flg:
                    flg = self.__last_object_singular[ind][1]
                    flg2 = self.__last_object_singular[ind][2]
                    temp_ref = self.__last_object_singular[ind][0]
                ind -= 1
            if flg == -1:
                wd = self.__last_object_singular[-1][0]
                self.__set_ent_renew(wd, 'OS', i,word_i)
                if self.__is_last_ch_vowel(wd):
                    wd += 'র'
                else:
                    wd += 'ের'

                return [self.__last_object_singular[-2][1]],[self.__last_object_singular[-2][2]],wd
            else:
                wd = temp_ref
                if self.__is_last_ch_vowel(wd):
                    wd += 'র'
                else:
                    wd += 'ের'
                self.__set_ent_renew(temp_ref, 'OS', i,word_i)
                return [flg],[flg2],wd
        elif (type == 'PP' or type == 'POP' or type == 'PPP') and (
                len(self.__last_person_plural) > 0 or len(self.__last_person_singular) >= 2):
            ind = len(self.__last_person_plural) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_person_plural[ind][1] != i:
                    flg = self.__last_person_plural[ind][1]
                    flg2= self.__last_person_plural[ind][2]
                    temp_ref = self.__last_person_plural[ind][0]
                elif flg != -1 and self.__last_person_plural[ind][1] == flg:
                    flg = self.__last_person_plural[ind][1]
                    flg2 = self.__last_person_plural[ind][2]
                    temp_ref = self.__last_person_plural[ind][0]
                ind -= 1
            if flg == -1:
                if (len(self.__last_person_singular) >= 2):
                    wd = (self.__last_person_singular[-2][0] + ' ও ' + self.__last_person_singular[-1][0])
                    self.__set_ent_renew(wd, 'PP', i,word_i)
                    return [self.__last_person_singular[-2][1],self.__last_person_singular[-1][1]],[self.__last_person_singular[-2][2],self.__last_person_singular[-1][2]],wd
                else:
                    return [-1],[-1],word
            else:
                if len(self.__last_person_singular) >= 2 and flg < self.__last_person_singular[-2][1]:

                    wd=(self.__last_person_singular[-2][0] + ' ও ' + self.__last_person_singular[-1][0])
                    self.__set_ent_renew(wd, 'PP', i,word_i)
                    return [self.__last_person_singular[-2][1],self.__last_person_singular[-1][1]],[self.__last_person_singular[-2][2],self.__last_person_singular[-1][2]],wd
                else:
                    self.__set_ent_renew(temp_ref, 'PP', i,word_i)
                    return [flg],[flg2],temp_ref
        elif (type == 'OP' or type == 'OOP' or type == 'OPP') and (
                len(self.__last_object_plural) > 0 or len(self.__last_object_singular) >= 2):
            ind = len(self.__last_object_plural) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                ind -= 1
                if flg == -1 and self.__last_object_plural[ind][1] != i:
                    flg = self.__last_object_plural[ind][1]
                    flg2= self.__last_object_plural[ind][2]
                    temp_ref = self.__last_object_plural[ind][0]
                elif flg != -1 and self.__last_object_plural[ind][1] == flg:
                    flg2 = self.__last_object_plural[ind][2]
                    flg = self.__last_object_plural[ind][1]
                    temp_ref = self.__last_object_plural[ind][0]
            if flg == -1:
                if (len(self.__last_object_singular) >= 2):
                    wd=((self.__last_object_singular[-2][0] + ' ও ' + self.__last_object_singular[-1][0]))
                    self.__set_ent_renew(wd, 'OP', i,word_i)
                    return [self.__last_object_singular[-2][1],self.__last_object_singular[-1][1]],[self.__last_object_singular[-2][2],self.__last_object_singular[-1][2]],wd
                else:
                    return [-1],[-1],word
            else:
                if len(self.__last_object_singular) >= 2 and flg < self.__last_object_singular[-2][1]:
                    wd=((self.__last_object_singular[-2][0] + ' ও ' + self.__last_object_singular[-1][0]))
                    self.__set_ent_renew(wd, 'OP', i,word_i)
                    return [self.__last_object_singular[-2][1], self.__last_object_singular[-1][1]],[self.__last_object_singular[-2][2], self.__last_object_singular[-1][2]] ,wd
                else:
                    self.__set_ent_renew(temp_ref, 'OP', i,word_i)
                    return [flg],[flg2],temp_ref
        elif type=='LOCS' and len(self.__last_loc_singular)>0:
            ind = len(self.__last_loc_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_loc_singular[ind][1] != i:
                    flg = self.__last_loc_singular[ind][1]
                    flg2= self.__last_loc_singular[ind][2]
                    temp_ref = self.__last_loc_singular[ind][0]
                elif flg != -1 and self.__last_loc_singular[ind][1] == flg:
                    flg = self.__last_loc_singular[ind][1]
                    flg2 = self.__last_loc_singular[ind][2]
                    temp_ref = self.__last_loc_singular[ind][0]
                ind -= 1
            if flg == -1:
                self.__set_ent_renew(self.__last_loc_singular[-1][0], 'LOCS', i,word_i)
                return [self.__last_loc_singular[-2][1]],[self.__last_loc_singular[-2][2]],self.__last_loc_singular[-1][0]
            else:
                self.__set_ent_renew(temp_ref, 'LOCS', i,word_i)
                return [flg],[flg2],temp_ref
        elif type=='LOCP' and (len(self.__last_loc_plural) > 0 or len(self.__last_loc_singular) >= 2):
            ind = len(self.__last_loc_plural) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_loc_plural[ind][1] != i:
                    flg = self.__last_loc_plural[ind][1]
                    flg2= self.__last_loc_plural[ind][2]
                    temp_ref = self.__last_loc_plural[ind][0]
                elif flg != -1 and self.__last_loc_plural[ind][1] == flg:
                    flg = self.__last_loc_plural[ind][1]
                    flg2= self.__last_loc_plural[ind][2]
                    temp_ref = self.__last_loc_plural[ind][0]
                ind -= 1
            if flg == -1:
                if (len(self.__last_loc_singular) >= 2):
                    wd = ((self.__last_loc_singular[-2][0] + ' ও ' + self.__last_loc_singular[-1][0]))
                    self.__set_ent_renew(wd, 'LOCP', i,word_i)
                    return [self.__last_loc_singular[-2][1],self.__last_loc_singular[-1][1]],[self.__last_loc_singular[-2][2],self.__last_loc_singular[-1][2]],wd
                else:
                    return [-1],[-1],word
            else:
                if len(self.__last_loc_singular) >= 2 and flg < self.__last_loc_singular[-2][1]:
                    wd=((self.__last_loc_singular[-2][0] + ' ও ' + self.__last_loc_singular[-1][0]))
                    self.__set_ent_renew(wd, 'LOCP', i,word_i)
                    return [self.__last_loc_singular[-2][1],self.__last_loc_singular[-1][1]],[self.__last_loc_singular[-2][2],self.__last_loc_singular[-1][2]],wd
                else:
                    self.__set_ent_renew(temp_ref, 'LOCP', i,word_i)
                    return [flg],[flg2],temp_ref
        elif type == 'ORGS' and len(self.__last_org_singular) > 0:
            ind = len(self.__last_org_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_org_singular[ind][1] != i:
                    flg = self.__last_org_singular[ind][1]
                    flg2= self.__last_org_singular[ind][2]
                    temp_ref = self.__last_org_singular[ind][0]
                elif flg != -1 and self.__last_org_singular[ind][1] == flg:
                    flg = self.__last_org_singular[ind][1]
                    flg2 = self.__last_org_singular[ind][2]
                    temp_ref = self.__last_org_singular[ind][0]
                ind -= 1
            if flg == -1:
                self.__set_ent_renew(self.__last_org_singular[-1][0], 'ORGS', i,word_i)
                return [self.__last_org_singular[-2][1]],[self.__last_org_singular[-2][2]],self.__last_org_singular[-1][0]
            else:
                self.__set_ent_renew(temp_ref, 'ORGS', i,word_i)
                return [flg],[flg2],temp_ref
        elif type == 'ORGP' and (len(self.__last_org_plural) > 0 or len(self.__last_org_singular) >= 2):
            ind = len(self.__last_org_plural) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_org_plural[ind][1] != i:
                    flg = self.__last_org_plural[ind][1]
                    flg2= self.__last_org_plural[ind][2]
                    temp_ref = self.__last_org_plural[ind][0]
                elif flg != -1 and self.__last_org_plural[ind][1] == flg:
                    flg = self.__last_org_plural[ind][1]
                    flg2= self.__last_org_plural[ind][2]
                    temp_ref = self.__last_org_plural[ind][0]
                ind -= 1
            if flg == -1:
                if (len(self.__last_org_singular) >= 2):
                    wd = ((self.__last_org_singular[-2][0] + ' ও ' + self.__last_org_singular[-1][0]))
                    self.__set_ent_renew(wd, 'ORGP', i,word_i)
                    return [self.__last_org_singular[-2][1],self.__last_org_singular[-1][1]],[self.__last_org_singular[-2][2],self.__last_org_singular[-1][2]],wd
                else:
                    return [-1],[-1],word
            else:
                if len(self.__last_org_singular) >= 2 and flg < self.__last_org_singular[-2][1]:
                    wd=((self.__last_org_singular[-2][0] + ' ও ' + self.__last_org_singular[-1][0]))
                    self.__set_ent_renew(wd, 'ORGP', i,word_i)
                    return [self.__last_org_singular[-2][1],self.__last_org_singular[-1][1]],[self.__last_org_singular[-2][2],self.__last_org_singular[-1][2]],wd
                else:
                    self.__set_ent_renew(temp_ref, 'ORGP', i,word_i)
                    return [flg],[flg2],temp_ref
        elif type == 'DATES' and len(self.__last_date_singular) > 0:
            ind = len(self.__last_date_singular) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_date_singular[ind][1] != i:
                    flg = self.__last_date_singular[ind][1]
                    flg2= self.__last_date_singular[ind][2]
                    temp_ref = self.__last_date_singular[ind][0]
                elif flg != -1 and self.__last_date_singular[ind][1] == flg:
                    flg = self.__last_date_singular[ind][1]
                    flg2= self.__last_date_singular[ind][2]
                    temp_ref = self.__last_date_singular[ind][0]
                ind -= 1
            if flg == -1:
                self.__set_ent_renew(self.__last_date_singular[-1][0], 'DATES', i,word_i)
                return [self.__last_date_singular[-2][1]],[self.__last_date_singular[-2][2]],self.__last_date_singular[-1][0]
            else:
                self.__set_ent_renew(temp_ref, 'DATES', i,word_i)
                return [flg],[flg2],temp_ref
        elif type == 'DATEP' and (len(self.__last_date_plural) > 0 or len(self.__last_date_singular) >= 2):
            ind = len(self.__last_date_plural) - 1
            flg = -1
            flg2=-1
            temp_ref = ""
            while (ind >= 0):
                if flg == -1 and self.__last_date_plural[ind][1] != i:
                    flg = self.__last_date_plural[ind][1]
                    flg2= self.__last_date_plural[ind][2]
                    temp_ref = self.__last_date_plural[ind][0]
                elif flg != -1 and self.__last_date_plural[ind][1] == flg:
                    flg = self.__last_date_plural[ind][1]
                    flg2= self.__last_date_plural[ind][2]
                    temp_ref = self.__last_date_plural[ind][0]
                ind -= 1
            if flg == -1:
                if (len(self.__last_date_singular) >= 2):
                    wd=((self.__last_date_singular[-2][0] + ' ও ' + self.__last_date_singular[-1][0]))
                    self.__set_ent_renew(wd, 'DATEP', i)
                    return [self.__last_date_singular[-2][1],self.__last_date_singular[-1][1]],[self.__last_date_singular[-2][2],self.__last_date_singular[-1][2]],wd
                else:
                    return [-1],[-1],(word)
            else:
                if len(self.__last_date_singular) >= 2 and flg < self.__last_date_singular[-2][1]:
                    wd=((self.__last_date_singular[-2][0] + ' ও ' + self.__last_date_singular[-1][0]))
                    self.__set_ent_renew(wd, 'DATEP', i,word_i)
                    return [self.__last_date_singular[-2][1],self.__last_date_singular[-1][1]],[self.__last_date_singular[-2][2],self.__last_date_singular[-1][2]],wd
                else:
                    self.__set_ent_renew(temp_ref, 'DATEP', i,word_i)
                    return [flg],[flg2],temp_ref
        elif type=='OWS' and len(self.__last_person_singular)>0:
            if self.__last_person_singular[-1][1]==i:
                return [self.__last_person_singular[-1][1]],[self.__last_person_singular[-1][2]],self.__last_person_singular[-1][0]
            return [-1],[-1],word
        elif type=='OWP' :
            if len(self.__last_person_plural)>0 and self.__last_person_plural[-1][1]==i:
                return [self.__last_person_plural[-1][1]],[self.__last_person_plural[-1][2]],self.__last_person_plural[-1][0]
            elif len(self.__last_person_singular)>=2 and self.__last_person_singular[-1][1]==i and self.__last_person_singular[-2][1]==i:
                return [self.__last_person_singular[-2][1],self.__last_person_singular[-1][1]],[self.__last_person_singular[-2][2],self.__last_person_singular[-1][2]],(self.__last_person_singular[-2][0]+' ও '+self.__last_person_singular[-1][0])
            return [-1],[-1],word
        return [-1],[-1],word


    # connector barano lagbe
    def __tokenize(self,text):
        sentences=self.__sentT.basic_tokenizer(text)
        seg_toks=['এবং','বলেছিলেন','']
        temp=[]
        for sent in sentences:
            if ' এবং ' in sent:
                sent2=sent.split('এবং')
                for i in range(len(sent2)):
                    if i==len(sent2)-1:
                        temp.append(sent2[i])
                        break
                    temp.append(sent2[i]+'এবং')
            else:
                temp.append(sent)
        return temp



    def resolve(self,text):
        sentences=self.__tokenize(text)
        mp,mp2=self.__get_entity(sentences)
        i=0
        self.__last_person_singular = []
        self.__last_person_plural = []
        self.__last_object_singular = []
        self.__last_object_plural = []
        self.__last_date_singular = []
        self.__last_org_singular = []
        self.__last_loc_plural = []
        self.__last_date_plural = []
        self.__last_org_plural = []
        resolve_text=[]
        resolve_pos=[]
        for sent in sentences:
            words=self.__wordT.basic_tokenizer(sent)
            map2=mp2[i]
            map1=mp[i]
            i+=1
            j=0
            ref=[]
            for x in range(len(words)):
                j+=1
                if map1.get(j) and self.__pro.isPronoun(words[x])[0]==False:
                    if words[x]=='ও' and map1.get(j+1) and map2.get(j-1):
                        self.__set_ent(map2[j-1][0],map2[j-1][1],i,j,map1[j+1][0])
                    else:
                        self.__set_ent(map1[j][0], map1[j][1], i,j)
                    ref.append(([],words[x]))
                elif self.__pro.isPronoun(words[x])[0]==True:
                    type=self.__pro.isPronoun(words[x])[1]
                    if type!='A':
                        ref.append(self.__single_resolve(type,i,words[x],j))
                    elif (type=='A') and j<len(words):
                        if self.__sta.isPer(words[j]) and self.__plu.is_plural(words[j]):
                            ref.append(self.__single_resolve('PP',i,words[x],j))
                        elif self.__sta.isPer(words[j]):
                            ref.append(self.__single_resolve('PS', i, words[x],j))
                        elif self.__sta.isLoc(words[j]) and self.__plu.is_plural(words[j]):
                            ref.append(self.__single_resolve('LOCP',i,words[x],j))
                        elif self.__sta.isLoc(words[j]):
                            ref.append(self.__single_resolve('LOCS', i, words[x],j))
                        elif self.__sta.isOrg(words[j]) and self.__plu.is_plural(words[j]):
                            ref.append(self.__single_resolve('ORGP',i,words[x],j))
                        elif self.__sta.isOrg(words[j]):
                            ref.append(self.__single_resolve('ORGS', i, words[x],j))
                        elif self.__sta.isDate(words[j]) and self.__plu.is_plural(words[j]):
                            ref.append(self.__single_resolve('DATEP',i,words[x],j))
                        elif self.__sta.isDate(words[j]):
                            ref.append(self.__single_resolve('DATES', i, words[x],j))
                        else:
                            ref.append(([],words[x]))
                else:
                     ref.append(([],words[x]))
            resolve_text.append(ref)
        return resolve_text












