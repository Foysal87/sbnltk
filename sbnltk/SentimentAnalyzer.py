'''
Types of SentimentAnalyzer
1. logisticRegression
2. LinearSVC
3. Multinomial_naive_bayes
5. Random Forest
4. Bert Sentiment
5. SVC
'''

from sbnltk.Downloader import downloader
import pickle
import pandas as pd
import numpy as np
from transformers import *
import tensorflow as tf
import tensorflow_addons as tfa
from sbnltk import sbnltk_default


class sentimentAnalyzer:
    __dl=downloader()
    __sentiment_models=[('LR','Logistic Regression'),('LSVC','Linear SVC'),
                      ('MNB','Multinomial naive bayes'),('RF','Random Forest'),('BERT','Bert Sentiment Analysis')
                      ]
    __root_path=sbnltk_default.sbnltk_root_path
    def all_sentiment_models(self):
        st='All Sentiment analysis models name with code\n'
        for sent in self.__sentiment_models:
            st+=sent[1]+' ::: '+sent[0]+'\n'
        return st
    def __LR(self,sentences):
        self.__dl.download('sentiment_LR',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('sentiment_vector',sbnltk_default.sbnltk_root_path+'model/')
        logreg = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_LR.pkl', 'rb'))
        vectorizer = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_vector.pkl', 'rb'))
        unknown_vectors = vectorizer.transform(sentences)
        unknown_words_df = pd.DataFrame(unknown_vectors.toarray(), columns=vectorizer.get_feature_names())
        pred=[]
        prop=[]
        for i in range(len(sentences)):
            pred.append(logreg.predict(unknown_words_df)[i])
            prop.append(logreg.predict_proba(unknown_words_df)[:, 1][i])
        return pred,prop
    def __LSVC(self,sentences):
        self.__dl.download('sentiment_LSVC', sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('sentiment_vector', sbnltk_default.sbnltk_root_path+'model/')
        svc = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_LSVC.pkl', 'rb'))
        vectorizer = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_vector.pkl', 'rb'))
        unknown_vectors = vectorizer.transform(sentences)
        unknown_words_df = pd.DataFrame(unknown_vectors.toarray(), columns=vectorizer.get_feature_names())
        pred = []
        for i in range(len(sentences)):
            pred.append(svc.predict(unknown_words_df)[i])
        return pred
    def __MNB(self,sentences):
        self.__dl.download('sentiment_MNB',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('sentiment_vector',sbnltk_default.sbnltk_root_path+'model/')
        mnb = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_MNB.pkl', 'rb'))
        vectorizer = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_vector.pkl', 'rb'))
        unknown_vectors = vectorizer.transform(sentences)
        unknown_words_df = pd.DataFrame(unknown_vectors.toarray(), columns=vectorizer.get_feature_names())
        pred = []
        prop = []
        for i in range(len(sentences)):
            pred.append(mnb.predict(unknown_words_df)[i])
            prop.append(mnb.predict_proba(unknown_words_df)[:, 1][i])
        return pred, prop
    def __RF(self,sentences):
        self.__dl.download('sentiment_RF',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('sentiment_vector',sbnltk_default.sbnltk_root_path+'model/')
        rf = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_RF.pkl', 'rb'))
        vectorizer = pickle.load(open(sbnltk_default.sbnltk_root_path+'model/sentiment_vector.pkl', 'rb'))
        unknown_vectors = vectorizer.transform(sentences)
        unknown_words_df = pd.DataFrame(unknown_vectors.toarray(), columns=vectorizer.get_feature_names())
        pred = []
        prop = []
        for i in range(len(sentences)):
            pred.append(rf.predict(unknown_words_df)[i])
            prop.append(rf.predict_proba(unknown_words_df)[:, 1][i])
        return pred, prop
    def __sentence_convert_data(self,data):
        tokenizer = BertTokenizer.from_pretrained(sbnltk_default.sbnltk_root_path+'model/sentiment_multilingual_vocab.txt')
        SEQ_LEN = 147
        tokens, masks, segments = [], [], []
        token = tokenizer.encode(data, max_length=SEQ_LEN, truncation=True, padding='max_length')
        num_zeros = token.count(0)
        mask = [1] * (SEQ_LEN - num_zeros) + [0] * num_zeros
        segment = [0] * SEQ_LEN
        tokens.append(token)
        segments.append(segment)
        masks.append(mask)
        tokens = np.array(tokens)
        masks = np.array(masks)
        segments = np.array(segments)
        return [tokens, masks, segments]

    def __b_predict(self,bert,sentences):
        pred=[]
        prop=[]
        for sent in sentences:
            data_x = self.__sentence_convert_data(sent)
            predict = bert.predict(data_x)
            predict_value = np.ravel(predict)
            predict_answer = np.round(predict_value, 0).item()
            if predict_answer == 0:
                pred.append(0)
                prop.append((1.0 - predict_value[0]))
            else:
                pred.append(1)
                prop.append((predict_value[0]))
        return pred,prop

    def __create_sentiment_bert(self):
        SEQ_LEN = 147
        model = TFBertModel.from_pretrained('bert-base-multilingual-cased')
        token_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_word_ids')
        mask_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_masks')
        segment_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_segment')
        bert_outputs = model([token_inputs, mask_inputs, segment_inputs])
        bert_outputs = bert_outputs[1]
        sentiment_first = tf.keras.layers.Dense(1, activation='sigmoid',
                                                kernel_initializer=tf.keras.initializers.TruncatedNormal(stddev=0.02))(
            bert_outputs)
        sentiment_model = tf.keras.Model([token_inputs, mask_inputs, segment_inputs], sentiment_first)
        opt = tfa.optimizers.RectifiedAdam(lr=2.0e-5, weight_decay=0.0025)
        sentiment_model.compile(optimizer=opt, loss=tf.keras.losses.BinaryCrossentropy(), metrics=['acc'])
        return sentiment_model
    def __BERT(self,sentence):
        self.__dl.download('sentiment_BERT',sbnltk_default.sbnltk_root_path+ 'model/')
        self.__dl.download('sentiment_multilingual_vocab',sbnltk_default.sbnltk_root_path+'model/')
        bert = self.__create_sentiment_bert()
        bert.load_weights(sbnltk_default.sbnltk_root_path+'model/sentiment_BERT.h5')
        return self.__b_predict(bert,sentence)
    def predict(self,model_code,sentences):
        if len(sentences)==0:
            raise ValueError('Empty list of Sentences is detected in Sentiment analysis!!')
        if model_code=='LR':
               pred,prop=self.__LR(sentences)
               return pred,prop
        elif model_code=='LSVC':
            pred=self.__LSVC(sentences)
            return pred
        elif model_code=='MNB':
            pred,prop=self.__MNB(sentences)
            return pred,prop
        elif model_code=='RF':
            pred,prop=self.__RF(sentences)
            return pred,prop
        elif model_code=='BERT':
            pred,prop=self.__BERT(sentences)
            return pred,prop
        else:
            raise ValueError('Model code Does not exist!!\n'+ self.all_sentiment_models())



