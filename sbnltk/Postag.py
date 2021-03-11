from sbnltk.Tokenizer import wordTokenizer
from sbnltk.Preprocessor import preprocessor
from sbnltk.Stemmer import stemmerOP
from sbnltk.Downloader import  downloader
from sbnltk import sbnltk_default
import pickle

class static_postag:
    __dl=downloader()
    __dict={}
    __stemmer=None
    __bp=preprocessor()
    __tokenizer=wordTokenizer()
    def __init__(self):
        self.__dl.download('postag_static',sbnltk_default.sbnltk_root_path+'dataset/')
        self.__stemmer=stemmerOP()
        path=sbnltk_default.sbnltk_root_path+'dataset/postag_static.txt'
        for word in open(path,'r'):
            word=word.replace('\n','')
            tokens=self.__tokenizer.basic_tokenizer(word)
            wd=tokens[0]
            val=tokens[-1]
            self.__dict[wd]=val
    def tag(self,sent):
        tokens=self.__tokenizer.basic_tokenizer(sent)
        ans=[]
        for word in tokens:
            if self.__bp.is_number(word):
                ans.append((word,'NUM'))
                continue
            if self.__dict.get(word):
               ans.append((word,self.__dict[word]))
               continue
            if self.__dict.get(self.__bp.word_normalize(word)) :
                ans.append((word, self.__dict[self.__bp.word_normalize(word)]))
                continue
            stem_word=self.__stemmer.stemWord(word)
            if self.__dict.get(stem_word):
               ans.append((word,self.__dict[stem_word]))
               continue
            ans.append((word,'unk'))
        return ans


class sklearn_postag:
    __dl=downloader()
    __bp=preprocessor()
    __sk_model=None
    def __init__(self):
        self.__dl.download('sklearn_postag',sbnltk_default.sbnltk_root_path+'model/')
        self.__sk_model = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sklearn_postag.pkl', 'rb'))
    def word2features(self,sent, i):
        return {
            'word': sent[i], 'is_first': i == 0, 'is_last': i == len(sent) - 1,
            'is_capitalized': sent[i][0].upper() == sent[i][0], 'is_all_caps': sent[i].upper() == sent[i],
            'is_all_lower': sent[i].lower() == sent[i],
            'prefix-1': sent[i][0], 'prefix-2': sent[i][:2], 'prefix-3': sent[i][:3],
            'suffix-1': sent[i][-1], 'suffix-2': sent[i][-2:], 'suffix-3': sent[i][-3:],
            'prev_word': '' if i == 0 else sent[i - 1], 'next_word': '' if i == len(sent) - 1 else sent[i + 1],
            'is_numeric': sent[i].isdigit()
        }
    def tag(self,text):
        if len(text)==0:
            return []
        words=text.split()
        sentence_features = [self.word2features(words, i) for i in range(len(words))]
        return list(zip(words, self.__sk_model.predict([sentence_features])[0]))
