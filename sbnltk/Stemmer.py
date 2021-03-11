from sbnltk.Preprocessor import preprocessor,StaticArray
from sbnltk.Tokenizer import wordTokenizer
import functools
import re
from sbnltk import sbnltk_default
from sbnltk.Downloader import downloader

rule_words = ['ই', 'ও', 'তো', 'কে', 'তে', 'রা', 'চ্ছি', 'চ্ছিল', 'চ্ছে', 'চ্ছিস', 'চ্ছিলেন', 'চ্ছ', 'য়েছে', 'েছ', 'েছে',
              'েছেন', 'রছ', 'রব', 'েল', 'েলো', 'ওয়া', 'েয়ে', 'য়', 'য়ে', 'েয়েছিল', 'েছিল', 'য়েছিল', 'েয়েছিলেন',
              'ে.েছিলেন', 'েছিলেন', 'লেন', 'দের', 'ে.ে', 'ের', 'ার', 'েন', 'বেন', 'িস', 'ছিস', 'ছিলি', 'ছি', 'ছে', 'লি',
              'বি', 'ে', 'টি', 'টির', 'েরটা', 'েরটার', 'টা', 'টার', 'গুলো', 'গুলোর', 'েরগুলো', 'েরগুলোর'
              'যোগ্য','কেই','েও','সহ','রা','ভাবে','কারি','কৃত','ই','কে','র','কি','েই','ভাবে','গুলো',
              'তে','েতে','গন','মুলক','সুচক','টুকু','টুকুই','গুলি','পদ','সমুহ','সংক্রান্ত','সংলগ্ন','সংশ্লিষ্ট',
              'সুত্রে','রুপে','ানুসারে','ানুযায়ি','তত্ত্','ি','মুখি','প্রতি','ভাবে','য়'
              ]
rule_dict = {"রছ":"র","রব":"র","েয়ে":"া","েয়েছিল":"া","েয়েছিলেন":"া","ে.েছিলেন":"া.","ে.ে":"া."}


class stemmerOP:
    __wordtokens = wordTokenizer()
    __word_vec = []
    __word_dict = {}
    __word_dict2 = {}
    __bp = preprocessor()
    __dl=downloader()
    def __init__(self):
        self.__dl.download('rootword_list',sbnltk_default.sbnltk_root_path+'dataset/')
        self.__dl.download('ner_static',sbnltk_default.sbnltk_root_path+'dataset/')
        for word in open(sbnltk_default.sbnltk_root_path + 'dataset/ner_static.txt', "r"):
            word = word.replace('\n', '')
            segment = word.split(' ')
            word = segment[:-1]
            for i in word:
                self.__word_dict[i]=1
        for word in open(sbnltk_default.sbnltk_root_path+'dataset/rootword_list.txt', "r"):
            word=word.replace('\n','')
            self.__word_dict2[word]=1
    def __search(self,word):
        if (self.__bp.word_normalize(word) in self.__word_dict) or (word in self.__word_dict) or (word in self.__word_dict2) or (self.__bp.word_normalize(word) in self.__word_dict2):
            return True
        return False
    def __bnCompare(self,item1,item2):
        return (len(item1)<len(item2))-(len(item1)>len(item2))

    def stemWord(self,word):
        try:
            if self.__word_dict2.get(word)!=None:
                return word
            suf_arr=[]
            for wd in rule_words:
                if re.search('.*' + wd + '$', word):
                    suf_arr.append(wd)
            suf_arr = sorted(suf_arr, key=functools.cmp_to_key(self.__bnCompare))
            if len(suf_arr)>0:
                for i in suf_arr:
                    if i in rule_dict:
                        ind = len(word) - len(i)
                        new_word=word[0:ind]+rule_dict[i]
                        if self.__search(new_word):
                            return new_word
                    ind = len(word) - len(i)
                    new_word = word[0:ind]
                    if len(new_word)==0:
                        return word
                    if self.__search(new_word):
                        return new_word
            return word
        except:
            print(f"{sbnltk_default.bcolors.FAIL}ERROR 101: Error in stemming!! {sbnltk_default.bcolors.ENDC}")
    def stemSent(self,sent):
        tokens=self.__wordtokens.basic_tokenizer(sent)
        temp_tokens=[]
        for i in tokens:
            temp_tokens.append(self.stemWord(i))
        result = ' '.join(temp_tokens)

        return result




