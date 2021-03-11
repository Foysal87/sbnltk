# Sentence Embedding 

## Sentence Embedding from word2vec

### Distance of two sentence
**INPUT:** sent1, sent2 \
**OUTPUT:**  float distance \
**PROCESS:** cosine distance(sent1,sent2) \
**USE CASE:** contextual distance

```python
from sbnltk.Sentence_embedding import sentence_embedding_from_word2vec
s2s=sentence_embedding_from_word2vec()
sentences=['আপনার বয়স কত','আমি তোমার বয়স জানতে চাই','আমার ফোন ভাল আছে','আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে']
for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(s2s.dist(sentences[i],sentences[j]),sentences[i],' ',sentences[j])

```

## Sentence Embedding Transformer Human translate data

```python
from sbnltk.Sentence_embedding import Bangla_sentence_embedding_hd
s2s=Bangla_sentence_embedding_hd()
sentences=['আপনার বয়স কত','আমি তোমার বয়স জানতে চাই','আমার ফোন ভাল আছে','আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে']
print(s2s.similarity_of_two_sentence(sentences[0],sentences[1]))
#0.83366
sentences_embeddings=s2s.encode_sentence_list(sentences)
for i in range(len(sentences)):
    j=i+1
    while j<len(sentences):
        s1=sentences[i]
        s2=sentences[j]
        print(s1,' -- ',s2,s2s.similarity_of_two_embedding(sentences_embeddings[s1],sentences_embeddings[s2]))
        j+=1
# আপনার বয়স কত  --  আমি তোমার বয়স জানতে চাই tensor([[0.8366]])
# আপনার বয়স কত  --  আমার ফোন ভাল আছে tensor([[0.2977]])
# আপনার বয়স কত  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.3517]])
# আমি তোমার বয়স জানতে চাই  --  আমার ফোন ভাল আছে tensor([[0.3500]])
# আমি তোমার বয়স জানতে চাই  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.3081]])
# আমার ফোন ভাল আছে  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.5784]])
```

## Sentence Embedding Transformer google translate data

```python
from sbnltk.Sentence_embedding import Bangla_sentence_embedding_gd
s2s=Bangla_sentence_embedding_gd()
sentences=['আপনার বয়স কত','আমি তোমার বয়স জানতে চাই','আমার ফোন ভাল আছে','আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে']
print(float(s2s.similarity_of_two_sentence(sentences[0],sentences[1])))
#0.8606657385826111
sentences_embeddings=s2s.encode_sentence_list(sentences)

for i in range(len(sentences)):
    j=i+1
    while j<len(sentences):
        s1=sentences[i]
        s2=sentences[j]
        print(s1,' -- ',s2,s2s.similarity_of_two_embedding(sentences_embeddings[s1],sentences_embeddings[s2]))
        j+=1
# আপনার বয়স কত  --  আমি তোমার বয়স জানতে চাই tensor([[0.8607]])
# আপনার বয়স কত  --  আমার ফোন ভাল আছে tensor([[0.1994]])
# আপনার বয়স কত  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.2581]])
# আমি তোমার বয়স জানতে চাই  --  আমার ফোন ভাল আছে tensor([[0.1960]])
# আমি তোমার বয়স জানতে চাই  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.2495]])
# আমার ফোন ভাল আছে  --  আপনার সেলফোনটি দুর্দান্ত দেখাচ্ছে tensor([[0.9281]])
```