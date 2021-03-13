# SBNLTK
SUST-Bangla Natural Language toolkit. A python module for Bangla NLP tasks.\
Demo Version : 1.0

## INSTALLATION
### PYPI INSTALLATION
```commandline
pip3 install sbnltk
```
### MANUAL INSTALLATION FROM GITHUB
* Clone this project
* Install all the requirements
* Call the setup.py from terminal

## What will you get here?
* Bangla Text Preprocessor
* Bangla word dust,punctuation,stop word removal
* Bangla word sorting according to Bangla or English alphabet
* Bangla word normalization
* Bangla word stemmer
* Bangla Sentiment analysis(logisticRegression,LinearSVC,Multilnomial_naive_bayes,Random_Forst)
* Bangla Sentiment analysis with Bert
* Bangla sentence pos tagger (static, sklearn)
* Bangla sentence pos tagger with BERT(Multilingual-cased,Multilingual uncased) 
* Bangla sentence NER(Static,sklearn)
* Bangla sentence NER with BERT(Bert-Cased, Multilingual Cased/Uncased)
* Bangla word word2vec(gensim,glove,fasttext)
* Bangla sentence embedding(Contexual,Transformer/Bert)
* Bangla Document Summarization(Feature based, Contexual, sementic Based)
* Bangla Bi-lingual project(Bangla to english google translator without blocking IP)
* Bangla document information Extraction

## TASKS, MODELS, ACCURACY, DATASET AND DOCS
|            TASK           |                               MODEL                               |    ACCURACY    |         DATASET         | About | Code DOCS |
|:-------------------------:|:-----------------------------------------------------------------:|:--------------:|:-----------------------:|:-----:|:---------:|
|        Preprocessor       | Punctuation, Stop Word, DUST removal Word normalization, others.. |     ------     |          -----          |       |[docs](https://github.com/Foysal87/sbnltk/blob/main/docs/preprocessor.md)         |
|      Word tokenizers      |               basic tokenizers Customized tokenizers              |      ----      |           ----          |       | [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Tokenizer.md#word-tokenizer)          |
|    Sentence tokenizers    |      Basic tokenizers Customized tokenizers Sentence Cluster      |      -----     |          -----          |       | [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Tokenizer.md#sentence-tokenizer)         |
|          Stemmer          |                             StemmerOP                             |      85.5%     |           ----          |       | [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Stemmer.md)          |
|     Sentiment Analysis    |                         logisticRegression                        |      88.5%     |         20,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentiment%20Analyzer.md#logistic-regression)         |
|                           |                             LinearSVC                             |      82.3%     |         20,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentiment%20Analyzer.md#linear-svc)         |
|                           |                      Multilnomial_naive_bayes                     |      84.1%     |         20,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentiment%20Analyzer.md#multinomial-naive-bayes)         |
|                           |                           Random Forest                           |      86.9%     |         20,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentiment%20Analyzer.md#random-forest)         |
|                           |                                BERT                               |      93.2%     |         20,000+         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentiment%20Analyzer.md#bert-sentiment-analysis)        |
|         POS tagger        |                           Static method                           |      55.5%     |     1,40,973  words     |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Postag.md#static-postag)        |
|                           |                      SK-LEARN classification                      |      81.2%     |     6,000+ sentences    |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Postag.md#sklearn-postag)        |
|                           |                        BERT-Multilingual-Cased                    |      69.2%     |          6,000+         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Postag.md#bert-multilingual-cased-postag)        |
|                           |                     BERT-Multilingual-Uncased                     |      78.7%     |          6,000+         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Postag.md#bert-multilingual-uncased-postag)        |
|         NER tagger        |                           Static method                           |      65.3%     |     4,08,837 Entity     |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/NER.md#static-ner)       |
|                           |                      SK-LEARN classification                      |      81.2%     |         65,000+         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/NER.md#sklearn-classification)        |
|                           |                             BERT-Cased                            |      79.2%     |         65,000+         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/NER.md#bert-cased-ner)        |
|                           |                       BERT-Mutilingual-Cased                      |      75.5%     |         65,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/NER.md#bert-multilingual-cased-ner)         |
|                           |                     BERT-Multilingual-Uncased                     |      90.5%     |         65,000+         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/NER.md#bert-multilingual-uncased-ner)         |
|       Word Embedding      |             Gensim-word2vec-100D- 1,00,00,000+ tokens             |        -       | 2,00,00,000+  sentences |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Word%20Embedding.md#gensim-word-embedding)         |
|                           |               Glove-word2vec-100D- 2,30,000+ tokens               |        -       |    5,00,000 sentences   |       | [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Word%20Embedding.md#fasttext-word-embedding)          |
|                           |                  fastext-word2vec-200D 3,00,000+                  |        -       |    5,00,000 sentences   |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Word%20Embedding.md#glove-word-embedding)         |
|     Sentence Embedding    |                   Contextual sentence embedding                   |        -       |          -----          |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentence%20Embedding.md#sentence-embedding-from-word2vec)         |
|                           |                      Transformer embedding_hd                     |        -       |   3,00,000+ human data  |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentence%20Embedding.md#sentence-embedding-transformer-human-translate-data)        |
|                           |                      Transformer embedding_gd                     |        -       |  3,00,000+ google data  |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Sentence%20Embedding.md#sentence-embedding-transformer-google-translate-data)        |
| Extractive  Summarization |                        Feature-based based                        | 70.0% f1 score |          ------         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Summarization.md#feature-based-model)         |
|                           |                Transformer sentence sentiment Based               |      67.0%     |          ------         |       | [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Summarization.md#word2vec_based_model)          |
|                           |                Word2vec--sentences contextual Based               |      60.0%     |          -----          |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Summarization.md#transformer_based_model)         |
|    Bi-lingual projects    |             google translator with large data detector            |      ----      |           ----          |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/Bangla%20translator.md#using-google-translator)         |
|   Information Extraction  |                        Static word features                       |        -       |                         |       |  [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/information%20extraction.md#feature-based-extraction)         |
|                           |                      Semantic and contextual                      |        -       |                         |       |   [docs](https://github.com/Foysal87/sbnltk/blob/main/docs/information%20extraction.md#contextual-information-extraction)       |


## Next releases after testing this demo

|              Task              |    Version   |
|:------------------------------:|:------------:|
|     Coreference Resolution     |    v1.1      |
|      Language translation      |    V1.1      |
|      Masked Language model     |    V1.1      |
| Information retrieval Projects |    V1.1      |
|       Entity Segmentation      |    v1.3      |
|   Factoid Question Answering   |    v1.2      |
|     Question Classification    |    v1.2      |
|    sentiment Word embedding    |    v1.3      |
|     So many others features    |     ---      |


## Package Installation

You have to install these packages manually, if you get any module error.
* simpletransformers
* fasttext

## Models
Everything is automated here. when you call a model for the first time, it will be downloaded automatically.

## With GPU or Without GPU
* With GPU, you can run any models without getting any warnings.
* Without GPU, You will get some warnings. But this will not affect in result.

## Motivation
With approximately 228 million native speakers and another 37 million as second language speakers,Bengali is the fifth most-spoken native 
language and the seventh most spoken language by total number of speakers in the world. But still it is a low resource language. Why?

## Dataset
We will release our all datasets soon.

## Trainer
I will release a trainer module soon.

## When will full version come?
Very soon. We are working on paper and improvement our modules. It will be released sequentially.

## About accuracy
Accuracy can be varied for the different datasets. We measure our model with random datasets but small scale. As human resources for this project are not so large.

## Contribute Here
* If you found any issue, please create an issue or contact with me.

