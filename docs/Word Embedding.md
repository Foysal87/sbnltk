# Word Embedding

## Gensim Word Embedding

### Get Vector
**INPUT:** word\
**OUTPUT:**  100 length float values vector \
**PROCESS:** Word to vector representation\
**USE CASE:** context word representation
```python
from sbnltk.word_embedding import gensim_word2vec_embedding
w2v=gensim_word2vec_embedding()
print(len(w2v.get_vector('তাঁকে')))
# 100
```

### Get nearest neighbors
**INPUT:** word, n \
**OUTPUT:**  list of words \
**PROCESS:** top n closure words \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import gensim_word2vec_embedding
w2v=gensim_word2vec_embedding()
print(w2v.get_nearest_neighbors('তাঁকে',n=5))
# ['তাঁকে', 'তাদেরকে', 'তাকে', 'যিশুকে', 'যীশুকে']
print(w2v.get_nearest_neighbors('তাঁকে',n=10))
# ['তাঁকে', 'তাদেরকে', 'তাকে', 'যিশুকে', 'যীশুকে', 'ঈশ্বরকে', 'তোমাদেরকে', 'একজনকে', 'আমাদেরকে', 'আমাকে']
```

### cosine distance 

**INPUT:** word1, word2 \
**OUTPUT:**  float distance \
**PROCESS:** 1 - cosine distance(word1,word2) \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import gensim_word2vec_embedding
w2v=gensim_word2vec_embedding()
print(w2v.cosine_distance('তাঁকে','তাদেরকে'))
# 0.7718406319618225
# higher value defines so close
# lower value defines so far
```


## Fasttext Word Embedding

### Get Vector
**INPUT:** word\
**OUTPUT:**  100 length float values vector \
**PROCESS:** Word to vector representation\
**USE CASE:** context word representation
```python
from sbnltk.word_embedding import fasttext_embedding
w2v=fasttext_embedding()
print(len(w2v.get_vector('তাঁকে')))
# 100
```

### Get nearest neighbors
**INPUT:** word, n \
**OUTPUT:**  list of pair(float,word) \
**PROCESS:** top n closure words with distance \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import fasttext_embedding
w2v=fasttext_embedding()
print(w2v.get_nearest_neighbors('তাঁকে',n=5))
# [(0.8493124842643738, 'তাঁকে,'), (0.8453188538551331, '"তাঁকে'), (0.8193084001541138, 'তাঁকেই'), (0.816943347454071, 'তাকে'), (0.7880011796951294, 'তাঁকেও')]
print(w2v.get_nearest_neighbors('তাঁকে',n=10))
# [(0.8493124842643738, 'তাঁকে,'), (0.8453188538551331, '"তাঁকে'), (0.8193084001541138, 'তাঁকেই'), (0.816943347454071, 'তাকে'), (0.7880011796951294, 'তাঁকেও'), (0.7862194180488586, 'তাঁদেরকে'), (0.7820371389389038, 'তাদেরকে'), (0.7681464552879333, 'যিশুকে'), (0.7661289572715759, 'যাঁকে'), (0.7522836923599243, 'ঈশ্বরকে')]
 
```

### cosine distance 

**INPUT:** word1, word2 \
**OUTPUT:**  float distance \
**PROCESS:** 1 - cosine distance(word1,word2) \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import fasttext_embedding
w2v=fasttext_embedding()
print(w2v.cosine_distance('তাঁকে','তাদেরকে'))
# 0.7718406319618225
# higher value defines so close
# lower value defines so far
```

## Glove Word Embedding

### Get Vector
**INPUT:** word\
**OUTPUT:**  100 length float values vector \
**PROCESS:** Word to vector representation\
**USE CASE:** context word representation
```python
from sbnltk.word_embedding import glove_embedding
w2v=glove_embedding()
print(len(w2v.get_vector('তাঁকে')))
# 100
```

### Get nearest neighbors
**INPUT:** word, n \
**OUTPUT:**  list of words \
**PROCESS:** top n closure words \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import glove_embedding
w2v=glove_embedding()
print(w2v.get_nearest_neighbors('তাঁকে',n=5))
print(w2v.get_nearest_neighbors('তাঁকে',n=10))
```

### cosine distance 

**INPUT:** word1, word2 \
**OUTPUT:**  float distance \
**PROCESS:** 1 - cosine distance(word1,word2) \
**USE CASE:** context word representation

```python
from sbnltk.word_embedding import glove_embedding
w2v=glove_embedding()
print(w2v.cosine_distance('তাঁকে','তাদেরকে'))
# higher value defines so close
# lower value defines so far
```
