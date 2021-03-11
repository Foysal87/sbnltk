# Parts of Speech Tags 

## All the Tag list
[check this site for knowing full details about tags](https://sites.google.com/site/partofspeechhelp/)
* NN -> Noun
* NNP -> Proper Noun
* NNS -> Plural Noun
* VB -> Verb
* PRP -> preposition
* DT -> Determiners
* CD -> Cardinal Numbers (Anything that indicates numeric includes number)
* RB -> Adverb
* IN -> Preposition
* CC -> Coordinating Conjunctions
* UH -> wh questions
* PRF -> anything indicates about myself
* JJ -> Adjective
* PRE -> prefix (ex. সহ,সাব)

## Static Postag

**INPUT:** Sentence \
**OUTPUT:**  list of pair(word,tag)  \
**PROCESS:** predict from static dataset \
**USE CASE:** Any NLP sector

```python
from sbnltk.Postag import static_postag
sp=static_postag()
print(sp.tag('তিনি এই কাজটি করতে চান না'))
# [('তিনি', 'PRP'), ('এই', 'JJ'), ('কাজটি', 'NN'), ('করতে', 'VB'), ('চান', 'VB'), ('না', 'VB')]
```

## sklearn Postag

**INPUT:** Sentence \
**OUTPUT:**  list of pair(word,tag)  \
**PROCESS:** predict from pretrained sk learn classification \
**USE CASE:** Any NLP sector
```python
from sbnltk.Postag import sklearn_postag
sp=sklearn_postag()
print(sp.tag('তিনি এই কাজটি করতে চান না'))
#[('তিনি', 'PRP'), ('এই', 'DT'), ('কাজটি', 'NN'), ('করতে', 'VB'), ('চান', 'VB'), ('না', 'DT')]
```

## Bert multilingual cased postag

**INPUT:** list of Sentence \
**OUTPUT:**  list of -> list of pair(word,tag)  \
**PROCESS:** predict from pretrain bert \
**USE CASE:** Any NLP sector
```python
from sbnltk.Postag_bert import bert_multilingual_cased_postag
sp=bert_multilingual_cased_postag()
print(sp.tag(['তিনি এই কাজটি করতে চান না']))
# [[('তিনি', 'PRP'), ('এই', 'DT'), ('কাজটি', 'VB'), ('করতে', 'VB'), ('চান', 'DT'), ('না', 'DT')]]
```

## Bert multilingual uncased postag

**INPUT:** list of Sentence \
**OUTPUT:**  list of -> list of pair(word,tag)  \
**PROCESS:** predict from pretrain bert \
**USE CASE:** Any NLP sector
```python
from sbnltk.Postag_bert import bert_Multilingual_Uncased_Postag
sp=bert_Multilingual_Uncased_Postag()
print(sp.tag(['তিনি এই কাজটি করতে চান না']))
# [[('তিনি', 'PRP'), ('এই', 'DT'), ('কাজটি', 'VB'), ('করতে', 'VB'), ('চান', 'DT'), ('না', 'DT')]]
```
