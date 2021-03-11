from sbnltk.Stemmer import stemmerOP
from sbnltk.Preprocessor import preprocessor
from sbnltk.Downloader import downloader
import pickle
from sbnltk import  sbnltk_default

class static_NER:
    __ner_static_data={}
    __bp = preprocessor()
    __stemmer = stemmerOP()
    __dl = downloader()
    def __init__(self):
        self.__dl.download('ner_static',sbnltk_default.sbnltk_root_path+'dataset/')
        for word in open(sbnltk_default.sbnltk_root_path+'dataset/ner_static.txt', "r"):
            word=word.replace('\n','')
            segment=word.split(' ')
            tag=segment[-1]
            word=segment[:-1]
            word=' '.join(word)

            self.__ner_static_data[word]=tag
    def tag(self,sentence):
        segment=sentence.split()
        stems=self.__stemmer.stemSent(sentence)
        stems=stems.split()
        i=0
        sentence_tags=[]
        while(i<len(segment)):
            j=len(segment)
            flg=0
            while(j>i):
                now=' '.join(segment[i:j])
                now2=' '.join(stems[i:j])
                if self.__ner_static_data.get(now)!=None:
                    sentence_tags.append((now,self.__ner_static_data[now]))
                    i=j-1
                    flg=1
                    break
                if self.__ner_static_data.get(now2)!=None:
                    sentence_tags.append((now, self.__ner_static_data[now2]))
                    i=j-1
                    flg=1
                j-=1
            if flg==0:
                sentence_tags.append((segment[i],'O'))
            i+=1
        return sentence_tags


class sklearn_NER:
    __dl=downloader()
    __bp=preprocessor()
    __sk_model=None
    def __init__(self):
        self.__dl.download('sklearn_ner',sbnltk_default.sbnltk_root_path+'model/')
        self.__sk_model = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sklearn_ner.pkl', 'rb'))
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

