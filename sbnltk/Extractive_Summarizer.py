'''
FBM
TBM
W2vBM
FBM+TBM
FBM+W2VBM
----------
with title
without title
------------
'''

from sbnltk.FBM_Information_Extraction import feature_based_information_extraction
from sbnltk.Semantic_Information_Extraction import information_extraction_word2vec
from sbnltk.Semantic_Information_Extraction import information_extraction_transformer_embedding
from sbnltk.Tokenizer import sentenceTokenizer

class feature_based_model:
    __fbm=None
    def __init__(self):
        self.__fbm=feature_based_information_extraction()

    def generate_summary(self,text,title=None,max_length=5):
        return self.__fbm.extract_text_to_text(text,title,max_length)

class word2vec_based_model:
    __w2vbm=None
    __sentT=None
    def __init__(self):
        self.__w2vbm=information_extraction_word2vec()
        self.__sentT=sentenceTokenizer()
    def generate_summary(self,text,title=None,max_length=5):
        sentences=self.__sentT.basic_tokenizer(text)
        if title==None:
            temp=self.__w2vbm.compute_information_from_single_centroid(sentences,max_length)
            sum_text = []
            for i in temp:
                sum_text.append(i[2])
            sum_text=self.__sentT.sentence_vector_to_text(sum_text)
            return sum_text
        temp= self.__w2vbm.compute_information_from_title(title,sentences,max_length)
        sum_text = []
        for i in temp:
            sum_text.append(i[2])
        sum_text=self.__sentT.sentence_vector_to_text(sum_text)
        return sum_text

class transformer_based_model:
    __tbm=None
    __sentT=None
    def __init__(self):
        self.__sentT=sentenceTokenizer()
        self.__tbm=information_extraction_transformer_embedding()
    def generate_summary(self,text,title=None,max_length=5):
        sentences=self.__sentT.basic_tokenizer(text)
        if title==None:
            temp=self.__tbm.compute_information_from_centroid(sentences,max_length)
            sum_text=[]
            for i in temp:
                sum_text.append(i[2])
            sum_text=self.__sentT.sentence_vector_to_text(sum_text)
            return sum_text
        temp= self.__tbm.compute_information_from_title(sentences,max_length)
        sum_text = []
        for i in temp:
            sum_text.append(i[2])
        sum_text=self.__sentT.sentence_vector_to_text(sum_text)
        return sum_text

