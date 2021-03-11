'''
WordTokenizer
    basic_tokenizer: only split words by space
    customized_tokenizer: split words, can remove punctuation (initially True), can make normalization(initially False), can remove dust(intitially False)

SentenceTokenizer:
    basic_tokenizer: only split by Bangla_fullstop
    customized_tokenizer: split sentences, can remove punctuation (initially True), can make normalization(initially False), can remove dust(intitially False)
    sentence_cluster: clustering sentences with max_length, can remove punctuation (initially True), can make normalization(initially False), can remove dust(intitially False)

'''



from sbnltk.Preprocessor import preprocessor
from sbnltk import sbnltk_default
bp=preprocessor()
class wordTokenizer:
    def basic_tokenizer(self,text):
        tokens = text.split()
        return tokens

    def customized_tokenizer(self,text,punc=True,norm=False,dust=False):
        if punc==True:
            text=bp.punctuation_remove(text)
        if norm==True:
            text=bp.word_normalize(text)
        tokens=text.split()
        try:
            if dust==True:
                temp_tokens=[]
                for i in tokens:
                    if len(bp.dust_removal(i))==0:
                        continue
                    i=bp.dust_removal(i)
                    temp_tokens.append(i)
                return temp_tokens
            else:
                return tokens
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 301: Error in Customized word Tokenizer!! {sbnltk_default.bcolors.ENDC}")
            return tokens

class sentenceTokenizer:

    __pre=preprocessor()

    def basic_tokenizer(self,text):
        text=text.replace('\n',' ')
        tokens = []
        s = ""
        bangla_fullstop = '0964'
        for c in text:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g == bangla_fullstop:
                tokens.append(s)
                s = ""
                continue
            s += c
        if len(s) > 0:
            tokens.append(s)
        return tokens

    def customized_tokenizer(self,text,punc=True,norm=False,dust=False):
        tokens=[]
        text = text.replace('\n', ' ')
        s=""
        bangla_fullstop = '0964'
        for c in text:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g==bangla_fullstop:
                tokens.append(s)
                s=""
                continue
            s+=c
        if len(s)>0:
            tokens.append(s)
        try:
            temp_tokens=[]
            for i in tokens:
                if punc==True:
                    i=bp.punctuation_remove(i)
                if norm==True:
                    i=bp.word_normalize(i)
                if len(bp.dust_removal_sent(i))!=0 and dust==True:
                    i=bp.dust_removal_sent(i)
                temp_tokens.append(i)
            return temp_tokens
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 302: Error in Customized Sentence Tokenizer!! {sbnltk_default.bcolors.ENDC}")
            return tokens

    def sentence_vector_to_text(self,sentences,full_stop=True):
        if full_stop==True:
            text=sbnltk_default.bangla_full_stop.join(sentences)
            text+=sbnltk_default.bangla_full_stop
        else:
            text=' '.join(sentences)
            text=self.__pre.extra_space_remove(text)
        return text

    def sentence_cluster(self,text,max_length=100,punc=True,norm=False,dust=False):
        tokens = []
        text = text.replace('\n', ' ')
        s = ""
        bangla_fullstop = '0964'
        for c in text:
            g = c.encode("unicode_escape")
            g = g.upper()
            g = g[2:]
            g = g.decode('utf-8')
            if g == bangla_fullstop:
                tokens.append(s)
                s = ""
                continue
            s += c
        if len(s) > 0:
            tokens.append(s)
        try:
            '''
            tmp_tokens: temporary tokens for returning
            word_tokens: taking word from each string
            tmp_sent: temporary sentence which length at most : max length
            '''
            tmp_tokens=[]
            for sent in tokens:
                if len(sent)>max_length:
                    l=len(sent)
                    word_tokens=sent.split()
                    tmp_sent=''
                    for w in word_tokens:
                        if len(str(tmp_sent+w))>max_length:
                            tmp_sent=tmp_sent[:-1]
                            tmp_tokens.append(tmp_sent)
                            tmp_sent=''
                        tmp_sent=tmp_sent+w+' '
                    tmp_tokens.append(tmp_sent)
                else:
                    tmp_tokens.append(sent)
            tmp_tokens2=[]
            for sent in tmp_tokens:
                if punc==True:
                    sent=bp.punctuation_remove(sent)
                if norm==True:
                    sent=bp.word_normalize(sent)
                if len(bp.dust_removal_sent(sent)) != 0 and dust == True:
                    sent = bp.dust_removal_sent(sent)
                tmp_tokens2.append(sent)
            return tmp_tokens2
        except:
            print(f"{sbnltk_default.bcolors.FAIL} ERROR 303: Error in Sentence clustering!! {sbnltk_default.bcolors.ENDC}")
            return tokens





