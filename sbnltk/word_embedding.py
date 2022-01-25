import numpy as np
from sbnltk import sbnltk_default
from sbnltk.Downloader import downloader
from scipy import spatial
import  fasttext
import pickle

class fasttext_embedding:
    __dl=downloader()
    __w2v=None
    def __init__(self):
        self.__dl.download('fasttext_w2v',sbnltk_default.sbnltk_root_path+'model/')
        self.__w2v=fasttext.load_model(sbnltk_default.sbnltk_root_path+'model/fasttext_w2v.model')
    def get_vector(self,word):
        try:
            return self.__w2v[word]
        except:
            raise ValueError('Sorry!! Word is not exist in vocab!!')
    def get_nearest_neighbors(self,word,n=5):
        return self.__w2v.get_nearest_neighbors(word,k=n)

    def cosine_distance(self,word1,word2):
        if word1==word2:
            return 1.0
        try:
            vec1=self.__w2v[word1]
        except:
            raise ValueError('Sorry!! 1st word is not exist in vocab!!')
        try:
            vec2=self.__w2v[word2]
        except:
            raise ValueError('Sorry!! 2nd word is not exist in vocab!!')

        return (1.0-spatial.distance.cosine(vec1,vec2))

class gensim_word2vec_embedding:
    __dl=downloader()
    __embeddings_dict = {}
    def __init__(self):
        self.__dl.download('gensim_w2v',sbnltk_default.sbnltk_root_path+'model/')
        path=sbnltk_default.sbnltk_root_path+'model/gensim_w2v.txt'
        with open(path, 'r') as f:
            for l in f:
                values = l.split()
                word = str(values[0])
                vec = np.asarray(values[1:], "float32")
                if len(vec)<100:
                    continue
                self.__embeddings_dict[word] = vec
    def get_vector(self,word):
        if word in self.__embeddings_dict:
           return self.__embeddings_dict[word]
        return np.zeros(100)
    def cosine_distance(self,word1,word2):
        if word1==word2:
            return 1.0
        vec1=np.zeros(100)
        vec2=np.zeros(100)
        flg=0
        if word1 in self.__embeddings_dict:
            vec1=self.__embeddings_dict[word1]
            flg+=1
        if word2 in self.__embeddings_dict:
            vec2=self.__embeddings_dict[word2]
            flg+=1
        if flg<=1:
            return 0.5
        d = 1.0 - spatial.distance.cosine(vec1,vec2)
        return d
    def get_nearest_neighbors(self,item,n):
        vec = []
        if item not in self.__embeddings_dict:
            vec.append(item)
            return vec
        result=sorted(self.__embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(self.__embeddings_dict[word], self.__embeddings_dict[item]))
        j=0
        for i in result:
           if j>=n:
             break
           vec.append(i)
           j+=1

        return vec

class glove_embedding:
    __dl=downloader()
    __embeddings_dict = {}
    def __init__(self):
        self.__dl.download('glove_embedding',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('glove_id2word', sbnltk_default.sbnltk_root_path + 'model/')
        path=sbnltk_default.sbnltk_root_path+'model/glove_embedding.pkl'
        model=pickle.load(open(path,'rb'))
        id2word=sbnltk_default.sbnltk_root_path+'model/glove_id2word.txt'
        with open(id2word, 'r') as f:
            for l in f:
                values = l.split()
                ind = int(values[0])
                word=str(values[1])
                vec = model[ind]
                if len(vec)<100:
                    continue
                self.__embeddings_dict[word] = vec

    def get_vector(self,word):
        if word in self.__embeddings_dict:
           return self.__embeddings_dict[word]
        return np.zeros(100)
    def cosine_distance(self,word1,word2):
        vec1=np.zeros(100)
        vec2=np.zeros(100)
        flg=0
        if word1 in self.__embeddings_dict:
            vec1=self.__embeddings_dict[word1]
            flg+=1
        if word2 in self.__embeddings_dict:
            vec2=self.__embeddings_dict[word2]
            flg+=1
        if flg==0:
            return 0.5
        d = 1.0 - spatial.distance.cosine(vec1,vec2)
        return d
    def get_nearest_neighbors(self,item,n):
        vec = []
        if item not in self.__embeddings_dict:
            vec.append(item)
            return vec
        result=sorted(self.__embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(self.__embeddings_dict[word], self.__embeddings_dict[item]))
        j=0
        for i in result:
           if j>=n:
             break
           vec.append(i)
           j+=1

        return vec


