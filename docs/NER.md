# Name Entity Tags

## Tag list
 * B-DATE : Begin of Date entity
 * B-LOC  : Begin of Location entity
 * B-OBJ  : Begin of object entity
 * B-ORG  : Begin of Organization entity
 * B-PER  : Begin of Person entity
 * E-DATE : End of Date entity
 * E-LOC  : End of Location entity
 * E-OBJ  : End of Object entity 
 * E-ORG  : End of Organization entity
 * E-PER  : End of Person entity
 * I-DATE : Intermediate of Date entity
 * I-LOC  : Intermediate of Location entity
 * I-OBJ  : Intermediate of Object entity 
 * I-ORG  : Intermediate of Organization entity
 * I-PER  : Intermediate of Person entity
 *   O    : Not a part of any entity
 * S-DATE : Single date entity
 * S-LOC  : Single location entity
 * S-OBJ  : Single object entity
 * S-ORG  : Single organization entity 
 * S-PER  : Single Person entity

## Static NER

**INPUT:** Sentence \
**OUTPUT:**  list of pair(word,tag)  \
**PROCESS:** predict from static dataset \
**USE CASE:** Any NLP sector
```python
from sbnltk.NER import static_NER
sn=static_NER()
print(sn.tag('গত ৩১শে জুলাই বাংলাদেশের ঢাকার ধোলাইপাড়ে শেখ মুজিবুর রহমানের একটি ভাস্কর্য স্থাপন নিয়ে ইসলামপন্থী দলগুলোর কট্টর অবস্থানের কারণে ক্ষমতাসীন আওয়ামী লীগের সাথে ধর্মভিত্তিক দলগুলোর টানাপোড়েন শুরু হয় '))
# [('গত', 'O'), ('৩১শে', 'O'), ('জুলাই', 'O'), ('বাংলাদেশের', 'LOC'), ('ঢাকার', 'LOC'), ('ধোলাইপাড়ে', 'O'), ('শেখ মুজিবুর রহমানের', 'PER'), ('একটি', 'O'), ('ভাস্কর্য', 'OBJ'), ('স্থাপন', 'O'), ('নিয়ে', 'O'), ('ইসলামপন্থী', 'O'), ('দলগুলোর', 'ORG'), ('কট্টর', 'O'), ('অবস্থানের', 'O'), ('কারণে', 'O'), ('ক্ষমতাসীন', 'O'), ('আওয়ামী লীগের', 'ORG'), ('সাথে', 'O'), ('ধর্মভিত্তিক', 'O'), ('দলগুলোর', 'ORG'), ('টানাপোড়েন', 'O'), ('শুরু', 'O'), ('হয়', 'O')]
```

## sklearn classification
**INPUT:** Sentence \
**OUTPUT:**  list of pair(word,tag)  \
**PROCESS:** predict from pretrained sk learn classification \
**USE CASE:** Any NLP sector
```python
from sbnltk.NER import sklearn_NER
sn=sklearn_NER()
print(sn.tag('গত ৩১শে জুলাই বাংলাদেশের ঢাকার ধোলাইপাড়ে শেখ মুজিবুর রহমানের একটি ভাস্কর্য স্থাপন নিয়ে ইসলামপন্থী দলগুলোর কট্টর অবস্থানের কারণে ক্ষমতাসীন আওয়ামী লীগের সাথে ধর্মভিত্তিক দলগুলোর টানাপোড়েন শুরু হয় '))
# [('গত', 'O'), ('৩১শে', 'B-DATE'), ('জুলাই', 'E-DATE'), ('বাংলাদেশের', 'S-LOC'), ('ঢাকার', 'S-LOC'), ('ধোলাইপাড়ে', 'O'), ('শেখ', 'B-PER'), ('মুজিবুর', 'I-PER'), ('রহমানের', 'E-PER'), ('একটি', 'O'), ('ভাস্কর্য', 'O'), ('স্থাপন', 'O'), ('নিয়ে', 'O'), ('ইসলামপন্থী', 'O'), ('দলগুলোর', 'O'), ('কট্টর', 'O'), ('অবস্থানের', 'O'), ('কারণে', 'O'), ('ক্ষমতাসীন', 'O'), ('আওয়ামী', 'B-ORG'), ('লীগের', 'E-ORG'), ('সাথে', 'O'), ('ধর্মভিত্তিক', 'O'), ('দলগুলোর', 'O'), ('টানাপোড়েন', 'O'), ('শুরু', 'O'), ('হয়', 'O')]
```

## Bert Cased NER
**INPUT:** list of Sentence \
**OUTPUT:**  list of -> list of pair(word,tag)  \
**PROCESS:** predict from pretrain bert \
**USE CASE:** Any NLP sector
```python
from sbnltk.Ner_bert import Bert_Cased_NER
sn=Bert_Cased_NER()
print(sn.tag(['গত ৩১শে জুলাই বাংলাদেশের ঢাকার ধোলাইপাড়ে শেখ মুজিবুর রহমানের একটি ভাস্কর্য স্থাপন নিয়ে ইসলামপন্থী দলগুলোর কট্টর অবস্থানের কারণে ক্ষমতাসীন আওয়ামী লীগের সাথে ধর্মভিত্তিক দলগুলোর টানাপোড়েন শুরু হয় ']))
# [[('গত', 'O'), ('৩১শে', 'B-DATE'), ('জুলাই', 'E-DATE'), ('বাংলাদেশের', 'S-LOC'), ('ঢাকার', 'S-LOC'), ('ধোলাইপাড়ে', 'O'), ('শেখ', 'B-PER'), ('মুজিবুর', 'B-PER'), ('রহমানের', 'E-PER'), ('একটি', 'O'), ('ভাস্কর্য', 'O'), ('স্থাপন', 'O'), ('নিয়ে', 'O'), ('ইসলামপন্থী', 'O'), ('দলগুলোর', 'O'), ('কট্টর', 'O'), ('অবস্থানের', 'O'), ('কারণে', 'O'), ('ক্ষমতাসীন', 'B-ORG'), ('আওয়ামী', 'E-ORG'), ('লীগের', 'E-ORG'), ('সাথে', 'O'), ('ধর্মভিত্তিক', 'O'), ('দলগুলোর', 'O'), ('টানাপোড়েন', 'O'), ('শুরু', 'O'), ('হয়', 'O')]]
```

## Bert Multilingual Cased NER

**INPUT:** list of Sentence \
**OUTPUT:**  list of -> list of pair(word,tag)  \
**PROCESS:** predict from pretrain bert \
**USE CASE:** Any NLP sector
```python
from sbnltk.Ner_bert import Bert_Multilingual_Cased_NER
sn=Bert_Multilingual_Cased_NER()
print(sn.tag(['গত ৩১শে জুলাই বাংলাদেশের ঢাকার ধোলাইপাড়ে শেখ মুজিবুর রহমানের একটি ভাস্কর্য স্থাপন নিয়ে ইসলামপন্থী দলগুলোর কট্টর অবস্থানের কারণে ক্ষমতাসীন আওয়ামী লীগের সাথে ধর্মভিত্তিক দলগুলোর টানাপোড়েন শুরু হয় ']))
# [[('গত', 'O'), ('৩১শে', 'B-DATE'), ('জুলাই', 'E-DATE'), ('বাংলাদেশের', 'S-LOC'), ('ঢাকার', 'S-LOC'), ('ধোলাইপাড়ে', 'O'), ('শেখ', 'B-PER'), ('মুজিবুর', 'E-PER'), ('রহমানের', 'O'), ('একটি', 'O'), ('ভাস্কর্য', 'O'), ('স্থাপন', 'O'), ('নিয়ে', 'O'), ('ইসলামপন্থী', 'O'), ('দলগুলোর', 'O'), ('কট্টর', 'O'), ('অবস্থানের', 'O'), ('কারণে', 'B-ORG'), ('ক্ষমতাসীন', 'E-ORG'), ('আওয়ামী', 'O'), ('লীগের', 'O'), ('সাথে', 'O'), ('ধর্মভিত্তিক', 'O'), ('দলগুলোর', 'O'), ('টানাপোড়েন', 'O'), ('শুরু', 'O'), ('হয়', 'O')]]
```

## Bert Multilingual Uncased NER
**INPUT:** list of Sentence \
**OUTPUT:**  list of -> list of pair map(word,tag)  \
**PROCESS:** predict from pretrain bert \
**USE CASE:** Any NLP sector
```python
from sbnltk.Ner_bert import Bert_Multilingual_Uncased_Ner
sn=Bert_Multilingual_Uncased_Ner()
print(sn.tag(['গত ৩১শে জুলাই বাংলাদেশের ঢাকার ধোলাইপাড়ে শেখ মুজিবুর রহমানের একটি ভাস্কর্য স্থাপন নিয়ে ইসলামপন্থী দলগুলোর কট্টর অবস্থানের কারণে ক্ষমতাসীন আওয়ামী লীগের সাথে ধর্মভিত্তিক দলগুলোর টানাপোড়েন শুরু হয় ']))
# [[{'গত': 'O'}, {'৩১শে': 'B-DATE'}, {'জুলাই': 'E-DATE'}, {'বাংলাদেশের': 'S-LOC'}, {'ঢাকার': 'S-LOC'}, {'ধোলাইপাড়ে': 'S-LOC'}, {'শেখ': 'B-PER'}, {'মুজিবুর': 'I-PER'}, {'রহমানের': 'E-PER'}, {'একটি': 'O'}, {'ভাস্কর্য': 'S-OBJ'}, {'স্থাপন': 'O'}, {'নিয়ে': 'O'}, {'ইসলামপন্থী': 'O'}, {'দলগুলোর': 'O'}, {'কট্টর': 'O'}, {'অবস্থানের': 'O'}, {'কারণে': 'O'}, {'ক্ষমতাসীন': 'O'}, {'আওয়ামী': 'B-ORG'}, {'লীগের': 'E-ORG'}, {'সাথে': 'O'}, {'ধর্মভিত্তিক': 'O'}, {'দলগুলোর': 'O'}, {'টানাপোড়েন': 'O'}, {'শুরু': 'O'}, {'হয়': 'O'}]]
```
