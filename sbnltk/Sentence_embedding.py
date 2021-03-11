from sbnltk.Tokenizer import wordTokenizer
from sbnltk.word_embedding import gensim_word2vec_embedding
import math
import os
import zipfile
from sbnltk.Downloader import downloader
from sentence_transformers import SentenceTransformer,util
from sbnltk import sbnltk_default

class sentence_embedding_from_word2vec:
    __w2v=None
    __tokenizer=None
    def __init__(self):
        self.__tokenizer=wordTokenizer()
        self.__w2v=gensim_word2vec_embedding()
    def dist(self,sent1,sent2):
        tokens1=self.__tokenizer.basic_tokenizer(sent1)
        tokens2=self.__tokenizer.basic_tokenizer(sent2)
        d=0
        for i in tokens1:
            mn=math.inf
            for j in tokens2:
                mn=min(mn,1.0-self.__w2v.cosine_distance(i,j))
            d+=mn
        return d
    # root sentence finding
    def root_sentence_finding(self,vec):
        ans=[]
        mx=0
        for sent1 in vec:
            temp=[]
            for sent2 in vec:
                temp.append(self.dist(sent1,sent2))
                mx=max(mx,self.dist(sent1,sent2))
            ans.append(temp)
        temp_ans=[]
        mx+=1.0
        for i in ans:
            temp=[]
            for j in i:
                temp.append((mx/(j+1.0)))
            temp_ans.append(temp)
        return temp_ans

class Bangla_sentence_embedding_hd:
    __dl=downloader()
    __model=None
    def __init__(self):
        if os.path.exists(sbnltk_default.sbnltk_root_path+'model/sentence_embedding_transformer')==False:
            self.__dl.download('sentence_embedding_transformer_hd', sbnltk_default.sbnltk_root_path + 'model/')
            with zipfile.ZipFile(sbnltk_default.sbnltk_root_path+'model/sentence_embedding_transformer_hd.zip', 'r') as file:
                file.extractall(sbnltk_default.sbnltk_root_path+'model/')
            os.remove(sbnltk_default.sbnltk_root_path+'model/sentence_embedding_transformer_hd.zip')
        self.__model=SentenceTransformer(sbnltk_default.sbnltk_root_path+'model/sentence_embedding_transformer')
    def encode_sentence_list(self,sentences):
        embeddings={}
        sentence_embeddings=self.__model.encode(sentences)
        for sentence, embedding in zip(sentences, sentence_embeddings):
            embeddings[sentence]=embedding
        return embeddings
    def similarity_of_two_sentence(self,sentence1,sentence2):
        embed=self.encode_sentence_list([sentence1,sentence2])
        return util.pytorch_cos_sim(embed[sentence1], embed[sentence2])
    def similarity_of_two_embedding(self,embedding1,embedding2):
        return util.pytorch_cos_sim(embedding1, embedding2)

class Bangla_sentence_embedding_gd:
    __dl = downloader()
    __model = None
    def __init__(self):
        if os.path.exists(sbnltk_default.sbnltk_root_path + 'model/Towhid-Sust-transformer') == False:
            self.__dl.download('sentence_embedding_transformer_gd', sbnltk_default.sbnltk_root_path + 'model/')
            with zipfile.ZipFile(sbnltk_default.sbnltk_root_path + 'model/sentence_embedding_transformer_gd.zip',
                                 'r') as file:
                file.extractall(sbnltk_default.sbnltk_root_path + 'model/')
            os.remove(sbnltk_default.sbnltk_root_path + 'model/sentence_embedding_transformer_gd.zip')
        self.__model = SentenceTransformer(sbnltk_default.sbnltk_root_path + 'model/Towhid-Sust-transformer')

    def encode_sentence_list(self, sentences):
        embeddings = {}
        sentence_embeddings = self.__model.encode(sentences)
        for sentence, embedding in zip(sentences, sentence_embeddings):
            embeddings[sentence] = embedding
        return embeddings
    def encode_single_sentence(self,sentence):
        return self.__model.encode(sentence)
    def similarity_of_two_sentence(self, sentence1, sentence2):
        embed = self.encode_sentence_list([sentence1, sentence2])
        return util.pytorch_cos_sim(embed[sentence1], embed[sentence2])

    def similarity_of_two_embedding(self, embedding1, embedding2):
        return util.pytorch_cos_sim(embedding1, embedding2)