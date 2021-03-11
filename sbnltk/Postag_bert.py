import torch
import numpy as np
from torch.utils.data import TensorDataset, DataLoader, SequentialSampler
from keras.preprocessing.sequence import pad_sequences
from pytorch_pretrained_bert import BertTokenizer
from sbnltk.Downloader import downloader
from sbnltk import  sbnltk_default
import zipfile
import os

class bert_multilingual_cased_postag:
    __dl = downloader()
    __model = None
    __tokenizer = None
    __device = None
    __tag2idx = {'CC': 10,'CD': 8, 'DT': 6, 'IN': 5, 'JJ': 0, 'NN': 4, 'NNP': 3,'NNS': 1, 'PRE': 12, 'PRF': 9, 'PRP': 13, 'RB': 7, 'VB': 2, 'WH': 11}
    __tags2vals = {}

    # isinstance
    def __init__(self):
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__dl.download('bert_multi_cased_postag', sbnltk_default.sbnltk_root_path + 'model/')
        self.__dl.download('bert_vocab_postag', sbnltk_default.sbnltk_root_path + 'model/')
        self.__tokenizer = BertTokenizer.from_pretrained(
            sbnltk_default.sbnltk_root_path + 'model/bert_vocab_postag.txt')
        self.__model = torch.load(sbnltk_default.sbnltk_root_path + 'model/bert_multi_cased_postag.pth',
                                  map_location=self.__device)
        for i in self.__tag2idx:
            self.__tags2vals[self.__tag2idx[i]] = i
        self.__model.eval()

    def tag(self, sentences):

        max_seq_len = 128  # tokens
        batch_s = 8
        all_sentence_tags = []
        for sentence in sentences:
            sentence = [sentence]
            words = sentence[0].split()
            false_labels = []
            for w in range(len(words)):
                false_labels.append('NN')
            labels = [false_labels]
            tokenized_texts = [self.__tokenizer.tokenize(sent) for sent in sentence]
            X = pad_sequences([self.__tokenizer.convert_tokens_to_ids(txt) for txt in tokenized_texts],
                              maxlen=max_seq_len, dtype="long", truncating="post", padding="post")
            Y = pad_sequences([[self.__tag2idx.get(l) for l in lab] for lab in labels],
                              maxlen=max_seq_len, value=self.__tag2idx["NN"], padding="post",
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
            temp_dict = []
            for i in range(len(words)):
                temp_dict.append((words[i], pred_tags[i]))
            all_sentence_tags.append(temp_dict)
        return all_sentence_tags

class bert_Multilingual_Uncased_Postag:
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
        if os.path.exists(sbnltk_default.sbnltk_root_path+'model/bert_multi_uncased_postag')==False:
            self.__dl.download('bert_multi_uncased_postag', sbnltk_default.sbnltk_root_path + 'model/')
            with zipfile.ZipFile(sbnltk_default.sbnltk_root_path+'model/bert_multi_uncased_postag.zip', 'r') as file:
                file.extractall(sbnltk_default.sbnltk_root_path+'model/')
            os.remove(sbnltk_default.sbnltk_root_path+'model/bert_multi_uncased_postag.zip')
        t_h=sbnltk_default.sbnltk_root_path+'model/bert_multi_uncased_postag/model_args.json'
        t_g=sbnltk_default.sbnltk_root_path+'model/bert_multi_uncased_postag/'
        self.__model = self.nermodel.NERModel('bert',t_g, use_cuda=self.__device, args=t_h)
    def tag(self,sentences):
        d, f = self.__model.predict(sentences)
        return d
