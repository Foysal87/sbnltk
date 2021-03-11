# tf(0.1)
# position(0.1)
# Numeric word(0.3)
# Sentence length(0.1)
# matched with title(0.1)
# exact title occurs(0.1)
from sbnltk.NER import sklearn_NER
from sbnltk.Stemmer import stemmerOP
from sbnltk.Tokenizer import wordTokenizer,sentenceTokenizer
from sbnltk.Preprocessor import preprocessor
from sbnltk.Postag import sklearn_postag

class feature_based_information_extraction:
    __pre=None
    __tokenizer=None
    __sentT=None
    __stemmer=None
    __sentences=[]
    __sent_pos={}
    __calc={}
    __title=""
    __nerT=None
    __posT=None
    def __init__(self):
        self.__stemmer=stemmerOP()
        self.__pre=preprocessor()
        self.__tokenizer=wordTokenizer()
        self.__sentT=sentenceTokenizer()
        self.__posT=sklearn_postag()
    def __term_frequency(self):
        word = {}
        total_word = 0
        for i in self.__sentences:
            tmp = self.__pre.punctuation_remove(i)
            tmp = self.__pre.stopword_remove(tmp)
            if len(tmp) == 0:
                continue
            tokens = self.__tokenizer.basic_tokenizer(tmp)
            for w in tokens:
                total_word += 1
                w = self.__stemmer.stemWord(w)
                if w in word:
                    word[w] += 1
                else:
                    word[w] = 1
        for i in self.__sentences:
            tmp = self.__pre.punctuation_remove(i)
            tmp = self.__pre.stopword_remove(tmp)
            if len(tmp) == 0:
                continue
            tokens = self.__tokenizer.basic_tokenizer(tmp)
            cnt = 0
            for w in tokens:
                cnt += word[self.__stemmer.stemWord(w)]
            self.__calc[i] += (cnt / total_word) * 0.1
        return
    def __is_number(self,word):
        v = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in word:
            if c in v:
                return True
        return False
    def __position(self):
        ln=len(self.__sentences)
        mid=int(0.7*ln)
        pos=1
        now=0.1
        dv1=0.1/mid
        for i in self.__sentences:
            if pos==mid:
                break
            self.__calc[i]+=now
            now-=dv1
            pos+=1

        pos=1
        dv2=.1/(ln-mid)
        now=dv2
        for i in self.__sentences:
            if pos<mid:
                pos+=1
                continue
            self.__calc[i]+=now
            now+=dv2
            pos+=1
        return
    def __Numeric_word(self):
        for i in self.__sentences:
            tokens = self.__tokenizer.basic_tokenizer(i)
            flg=0
            for w in tokens:
                if self.__is_number(w):
                    flg=1
                    break
            if flg:
                self.__calc[i]+=0.1
        return
    def __sentence_length(self):
        for i in self.__sentences:
            if len(i)>50:
                continue
            self.__calc[i]+=((50-len(i))/50)*0.1
        return
    def __matched_with_title(self):
        title=self.__stemmer.stemSent(self.__title)
        title_tokens=self.__tokenizer.basic_tokenizer(title)

        for i in self.__sentences:
            cnt=0
            e_title=0
            now=title_tokens[0]
            pos=0
            tmp={}
            tm_sent=i
            i=self.__stemmer.stemSent(i)
            tokens=self.__tokenizer.basic_tokenizer(i)
            for w in tokens:
                if w in title_tokens:
                    if w not in tmp:
                        cnt+=1
                        tmp[w]=1
                if pos>=len(title_tokens):
                    continue
                if w==now:
                    e_title+=1
                    pos+=1
                    if pos<len(title_tokens):
                        now=title_tokens[pos]
            self.__calc[tm_sent]+=(len(tmp)/len(title_tokens))*0.1
            if pos>=len(title_tokens):
                self.__calc[tm_sent]+=0.1
        return
    def __count_ner_tags_with_tag(self,sentence):
        cnt=0
        for i in sentence:
            if i[1]!='O':
                cnt+=1
        return cnt

    def __count_ner(self):
        self.__nerT=sklearn_NER()
        for sent in self.__sentences:
            tags = self.__nerT.tag(sent)
            cnt = self.__count_ner_tags_with_tag(tags)
            if len(tags) > 0:
                self.__calc[sent] += float(float(cnt * 0.1) / len(tags))
        return

    def __count_postag(self):
        for sent in self.__sentences:
            tags=self.__posT.tag(sent)
            cnt=0
            for i in tags:
                if i[1]=='NN' or i[1]=='NNP':
                    cnt+=1
            if len(tags)>0:
                self.__calc[sent]+=float(float(cnt*0.1)/float(len(tags)))
        return
    def __update(self):
        pos = 0
        for i in self.__sentences:
            self.__calc[i] = 0.0
            self.__sent_pos[i] = pos
            pos += 1
        self.__term_frequency()
        self.__position()
        self.__Numeric_word()
        self.__sentence_length()
        if len(self.__title)!=0:
            self.__matched_with_title()
        self.__count_ner()
        self.__count_postag()

    '''
        param: text, 
               title = None(default)
               max_output_sent= 5 (default)
        return :
            extracted text 
        '''
    def extract_text_to_text(self,text,title=None,max_extract_sent=5):
        if len(text)==0:
            raise ValueError('Null Text for information Extraction')
        if title!=None:
            self.__title=title
        text=self.__pre.extra_space_remove(text)
        sentences=self.__sentT.basic_tokenizer(text)
        self.__sentences=sentences
        self.__update()
        vec=[]
        for i in sentences:
            vec.append((self.__calc[i],self.__sent_pos[i]))
        top_sentences = sorted(vec, reverse=True)
        max_extract_sent=min(max_extract_sent,len(text))
        ans_vec=[]
        for i in range(len(top_sentences)):
            if i>=max_extract_sent:
                break
            ans_vec.append(top_sentences[i][1])
        ans_temp_vec=sorted(ans_vec)
        ans_vec=[]
        for i in ans_temp_vec:
            ans_vec.append(sentences[i])
        extract_text=self.__sentT.sentence_vector_to_text(ans_vec)
        return extract_text

    '''
    param: text, 
           title = None(default)
           max_output_sent= 5 (default)
    return :
        sorted vector (higher to lower)
        1st position: score of that sentence
        2nd position: sentence
        3rd position: position of sentence
    '''
    def extract_text_to_vector(self,text,title=None,max_extract_sent=5):
        if len(text)==0:
            raise ValueError('Null Text for information Extraction')
        text = self.__pre.extra_space_remove(text)
        if title!=None:
            self.__title=title
        sentences=self.__sentT.basic_tokenizer(text)
        self.__sentences=sentences
        self.__update()
        vec=[]
        for i in sentences:
            vec.append((self.__calc[i],i,self.__sent_pos[i]))
        max_extract_sent = min(max_extract_sent, len(text))
        top_sentences = sorted(vec, reverse=True)[:max_extract_sent]
        return top_sentences





