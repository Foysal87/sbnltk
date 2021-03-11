from Sentence_embedding import sentence_embedding_from_word2vec,Bangla_sentence_embedding_gd

class information_extraction_word2vec:
    __s_w2v=None
    def __init__(self):
        self.__s_w2v=sentence_embedding_from_word2vec()
    def compute_information_from_title(self,title,sentences,k):
        if (len(sentences) == 0):
            return []
        dict = {}
        vec = []
        for k in range(min(k, len(sentences))):
            low = 10000.0
            ind = 0
            i = 0
            for sent in sentences:
                d = self.__s_w2v.dist(sent, title)
                if d < low and (i not in dict):
                    low = d
                    ind = i
                i += 1
            dict[ind] = 1
            vec.append([low, ind, sentences[ind]])
        return sorted(vec)
    def __compute_centroid(self,sentences):
        low = 10000.0
        ind = 0

        for i in range(len(sentences)):
            sum = 0.0
            for j in range(len(sentences)):
                sum += self.__s_w2v.dist(sentences[i], sentences[j])
            if sum < low:
                low = sum
                ind = i
        return ind
    def compute_information_from_single_centroid(self,sentences,k):
        if(len(sentences)==0):
            return []
        title_ind=self.__compute_centroid(sentences)
        return self.compute_information_from_title(sentences[title_ind],sentences,k)


    def compute_information_from_neighbours(self,sentences,k):
        if (len(sentences) == 0):
            return []
        title_ind = self.__compute_centroid(sentences)
        dict = {}
        dict[title_ind] = 1
        title = sentences[title_ind]
        low = 10000.0
        ind = 0
        i = 0
        vec = []
        for k in range(min(k, len(sentences))):
            i = 0
            for sent in sentences:
                d = self.__s_w2v.dist(sent, title)
                if d < low and (i not in dict):
                    low = d
                    ind = i
                i += 1
            dict[ind] = 1
            vec.append([low, ind, sentences[ind]])
        return sorted(vec)

class information_extraction_transformer_embedding:
    __s_tse=None
    def __init__(self):
        self.__s_tse = Bangla_sentence_embedding_gd()

    def n_gram_sentence(self,title,sentences,n):
        title_embeddings = self.__s_tse.encode_single_sentence(title)
        sentence_embeddings = self.__s_tse.encode_sentence_list(sentences)
        top_sentences = []
        done_sentence = []
        embedding = title_embeddings
        for i in range(len(sentences) - 1):
            j = 0
            mx = 0.0
            temp = ""
            ind = 0
            for sentence in sentences:
                if j in done_sentence:
                    j += 1
                    continue
                sim = self.__s_tse.similarity_of_two_embedding(embedding, sentence_embeddings[sentence])
                if sim > mx:
                    mx = sim
                    temp = sentence
                    embedding = sentence_embeddings[sentence]
                    ind = j
                j += 1
            done_sentence.append(ind)
            top_sentences.append([mx, ind, temp])
            n=min(n,len(sentences))
        return top_sentences[:n]
    def compute_information_from_title(self,title,sentences,k):
        title_embeddings = self.__s_tse.encode_single_sentence(title)
        sentence_embeddings = self.__s_tse.encode_sentence_list(sentences)
        top_sentences = []
        ind = 0
        k=min(k,len(sentences))
        for sentence in sentences:
            sim = self.__s_tse.similarity_of_two_embedding(title_embeddings, sentence_embeddings[sentence])
            top_sentences.append([sim, ind, sentence])
            ind += 1
        top_sentences = sorted(top_sentences, reverse=True)
        return top_sentences[:k]
    def __compute_centroid(self,sentences):
        high = 0.0
        ind = 0
        x=0
        sentence_embeddings = self.__s_tse.encode_sentence_list(sentences)
        for i in sentences:
            sum = 0.0
            for j in sentences:
                sum += self.__s_tse.similarity_of_two_embedding(sentence_embeddings[i], sentence_embeddings[j])
            if sum > high:
                high = sum
                ind = x
            x+=1
        return ind
    def compute_information_from_centroid(self,sentences,k):
        title=sentences[self.__compute_centroid(sentences)]
        k = min(k, len(sentences))
        return self.compute_information_from_title(title,sentences,k)