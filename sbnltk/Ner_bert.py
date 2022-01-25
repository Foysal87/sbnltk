
import torch
import zipfile
import numpy as np
from torch.utils.data import TensorDataset, DataLoader, SequentialSampler
from keras.preprocessing.sequence import pad_sequences
from pytorch_pretrained_bert import BertTokenizer
import os
from sbnltk.Downloader import downloader
from sbnltk import  sbnltk_default


class Bert_Cased_NER:
    __dl=downloader()
    __model=None
    __tokenizer = None
    __device = None
    __tag2idx = {'B-DATE': 3, 'B-LOC': 9, 'B-OBJ': 18, 'B-ORG': 12, 'B-PER': 4, 'E-DATE': 6, 'E-LOC': 14, 'E-OBJ': 5,
               'E-ORG': 7, 'E-PER': 17,
               'I-DATE': 1, 'I-LOC': 20, 'I-OBJ': 19, 'I-ORG': 2, 'I-PER': 11, 'O': 8, 'S-DATE': 15, 'S-LOC': 10,
               'S-OBJ': 13, 'S-ORG': 0, 'S-PER': 16}
    __tags2vals = {}
    # isinstance
    def __init__(self):
        self.__device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__dl.download('bert_cased_ner_model',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('bert_cased_ner_vocab',sbnltk_default.sbnltk_root_path+'model/')
        self.__tokenizer = BertTokenizer.from_pretrained(sbnltk_default.sbnltk_root_path+'model/bert_cased_ner_vocab.txt')
        self.__model = torch.load(sbnltk_default.sbnltk_root_path+'model/bert_cased_ner_model.pth', map_location=self.__device)
        for i in self.__tag2idx:
            self.__tags2vals[self.__tag2idx[i]] = i
        self.__model.eval()
    def tag(self,sentences):

        max_seq_len = 80  # tokens
        batch_s = 8
        all_sentence_tags = []
        for sentence in sentences:
            sentence = [sentence]
            words = sentence[0].split()
            false_labels = []
            for w in range(len(words)):
                false_labels.append('O')
            labels = [false_labels]
            tokenized_texts = [self.__tokenizer.tokenize(sent) for sent in sentence]
            X = pad_sequences([self.__tokenizer.convert_tokens_to_ids(txt) for txt in tokenized_texts],
                              maxlen=max_seq_len, dtype="long", truncating="post", padding="post")
            Y = pad_sequences([[self.__tag2idx.get(l) for l in lab] for lab in labels],
                              maxlen=max_seq_len, value=self.__tag2idx["O"], padding="post",
                              dtype="long", truncating="post")
            attention_masks = [[float(i > 0) for i in ii] for ii in X]
            X_train = torch.tensor(X)
            Y_train = torch.tensor(Y)
            Mask_train = torch.tensor(attention_masks)
            data_valid = TensorDataset(X_train, Mask_train, Y_train)
            data_valid_sampler = SequentialSampler(data_valid)
            DL_valid = DataLoader(data_valid, sampler=data_valid_sampler, batch_size=batch_s)
            predictions = []
            for batch in DL_valid:
                batch = tuple(t.to(self.__device) for t in batch)
                b_input_ids, b_input_mask, b_labels = batch
                with torch.no_grad():
                    logits = self.__model(b_input_ids, token_type_ids=None,
                                   attention_mask=b_input_mask)
                logits = logits.detach().cpu().numpy()
                predictions.extend([list(p) for p in np.argmax(logits, axis=2)])
            pred_tags = [[self.__tags2vals[p_i] for p_i in p] for p in predictions]
            pred_tags = pred_tags[0][:(len(words))]
            temp_dict=[]
            for i in range(len(words)):
                temp_dict.append((words[i],pred_tags[i]))
            all_sentence_tags.append(temp_dict)
        return all_sentence_tags


class Bert_Multilingual_Cased_NER:
    __dl=downloader()
    __model=None
    __tokenizer = None
    __device = None
    __tag2idx = {'B-DATE': 19, 'B-LOC': 13, 'B-OBJ': 17, 'B-ORG': 15, 'B-PER': 12, 'E-DATE': 2, 'E-LOC': 7, 'E-OBJ': 6,
               'E-ORG': 10, 'E-PER': 9, 'I-DATE': 4,
               'I-LOC': 3, 'I-OBJ': 1, 'I-ORG': 20, 'I-PER': 16, 'O': 11, 'S-DATE': 0, 'S-LOC': 8, 'S-OBJ': 14,
               'S-ORG': 18, 'S-PER': 5}
    __tags2vals = {}
    # isinstance
    def __init__(self):
        self.__device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__dl.download('bert_multilingual_cased_ner_model',sbnltk_default.sbnltk_root_path+'model/')
        self.__dl.download('bert_multilingual_cased_ner_vocab',sbnltk_default.sbnltk_root_path+'model/')
        self.__tokenizer = BertTokenizer.from_pretrained(sbnltk_default.sbnltk_root_path+'model/bert_multilingual_cased_ner_vocab.txt')
        self.__model = torch.load(sbnltk_default.sbnltk_root_path+'model/bert_multilingual_cased_ner_model.pth', map_location=self.__device)
        for i in self.__tag2idx:
            self.__tags2vals[self.__tag2idx[i]] = i
        self.__model.eval()
    def tag(self,sentences):

        max_seq_len = 128  # tokens
        batch_s = 8
        all_sentence_tags = []
        for sentence in sentences:
            sentence = [sentence]
            words = sentence[0].split()
            false_labels = []
            for w in range(len(words)):
                false_labels.append('O')
            labels = [false_labels]
            tokenized_texts = [self.__tokenizer.tokenize(sent) for sent in sentence]
            X = pad_sequences([self.__tokenizer.convert_tokens_to_ids(txt) for txt in tokenized_texts],
                              maxlen=max_seq_len, dtype="long", truncating="post", padding="post")
            Y = pad_sequences([[self.__tag2idx.get(l) for l in lab] for lab in labels],
                              maxlen=max_seq_len, value=self.__tag2idx["O"], padding="post",
                              dtype="long", truncating="post")
            attention_masks = [[float(i > 0) for i in ii] for ii in X]
            X_train = torch.tensor(X)
            Y_train = torch.tensor(Y)
            Mask_train = torch.tensor(attention_masks)
            data_valid = TensorDataset(X_train, Mask_train, Y_train)
            data_valid_sampler = SequentialSampler(data_valid)
            DL_valid = DataLoader(data_valid, sampler=data_valid_sampler, batch_size=batch_s)
            predictions = []
            for batch in DL_valid:
                batch = tuple(t.to(self.__device) for t in batch)
                b_input_ids, b_input_mask, b_labels = batch
                with torch.no_grad():
                    logits = self.__model(b_input_ids, token_type_ids=None,
                                   attention_mask=b_input_mask)
                logits = logits.detach().cpu().numpy()
                predictions.extend([list(p) for p in np.argmax(logits, axis=2)])
            pred_tags = [[self.__tags2vals[p_i] for p_i in p] for p in predictions]
            pred_tags = pred_tags[0][:(len(words))]
            temp_dict=[]
            for i in range(len(words)):
                temp_dict.append((words[i],pred_tags[i]))
            all_sentence_tags.append(temp_dict)
        return all_sentence_tags


class Bert_Multilingual_Uncased_Ner:
    __model = None
    __dl=downloader()
    __device=True if torch.cuda.is_available() else False
    __module_found=1
    try:
        import simpletransformers.ner.ner_model as nermodel
        __module_found=1
    except:
        __module_found=0
    def __init__(self):
        if self.__module_found==0:
            raise ValueError('Please install simpletransformers!! install Command: pip3 install simpletransformers')
        if os.path.exists(sbnltk_default.sbnltk_root_path+'model/bert_multilingual_uncased')==False:
            self.__dl.download('bert_multilingual_uncased_ner_model', sbnltk_default.sbnltk_root_path + 'model/')
            with zipfile.ZipFile(sbnltk_default.sbnltk_root_path+'model/bert_multilingual_uncased_ner_model.zip', 'r') as file:
                file.extractall(sbnltk_default.sbnltk_root_path+'model/')
            os.remove(sbnltk_default.sbnltk_root_path+'model/bert_multilingual_uncased_ner_model.zip')
        t_h=sbnltk_default.sbnltk_root_path+'model/bert_multilingual_uncased/model_args.json'
        t_g=sbnltk_default.sbnltk_root_path+'model/bert_multilingual_uncased/'
        self.__model = self.nermodel.NERModel('bert',t_g, use_cuda=self.__device, args=t_h)
    def tag(self,sentences):
        d, f = self.__model.predict(sentences)
        return d

