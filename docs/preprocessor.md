# Preprocessor

## Punctuation Remove

**INPUT:** Text \
**OUTPUT:** Text \
**PROCESS:** Remove all the punctuation from text \
**USE CASE:** Clean Text 

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.punctuation_remove('রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়
```

## Dust removal

**INPUT:** Word \
**OUTPUT** Word \
**PROCESS:** Remove all the characters from the Word without Bangla character \
**USE CASE** Clean Text

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.dust_removal('রবীন্দ্রনাথকেab1%'))
# OUTPUT: রবীন্দ্রনাথকে
```

## Stopword Remove

**INPUT:** Text \
**OUTPUT** Text \
**PROCESS:** Remove all the stop words from the Text \
**USE CASE** Frequency models, TF-IDF models, so many.

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.stopword_remove('রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# OUTPUT: রবীন্দ্রনাথকে গুরুদেব, কবিগুরু বিশ্বকবি অভিধায় ভূষিত হয়।
```

## Word Normalize

**INPUT:** Word/Text \
**OUTPUT** Word/Text \
**PROCESS:** Replace all the Same sound characters with unique character \
**USE CASE** Frequency models, TF-IDF models, Any word searching models,etc .

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.word_normalize('রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# OUTPUT: রবিন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভুষিত করা হয়।
```

## Bangla to English Conversion

**INPUT:** Word \
**OUTPUT** Banglish Word \
**PROCESS:** Convert Every bangla character with english character \
**USE CASE** speech, writing bangla word in english

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.bangla_to_english_Conversion('রবীন্দ্রনাথ'))
# OUTPUT: rabindranath
```

## Bangla word check

**INPUT:** Word \
**OUTPUT** Boolean \
**PROCESS:** Check is any bangla character exist in this word \
**USE CASE** Clean text

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.isBangla('রবীন্দ্রনাথ'))
# True
print(p.isBangla('abced1'))
# False
```


## Bangla words sort according to english alphabet

**INPUT:** list \
**OUTPUT** list \
**PROCESS:** Sort the list \
**USE CASE:** Searching algorithm, Representation

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.bn_word_sort_en_sys(['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']))
# ['১', 'ভারী', 'বিভিন্ন', 'বর্ষণে', 'দেখা', 'দেয়', 'এলাকায়', 'ঘণ্টার', 'জলাবদ্ধতা', 'রাজধানীর', 'সোমবার']
```

## Bangla words sort according to Bangla alphabet

**INPUT:** list \
**OUTPUT** list \
**PROCESS:** Sort the list \
**USE CASE:** Searching algorithm, Representation

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.bn_word_sort_bn_sys(['১', 'ঘণ্টার', 'ভারী' ,'বর্ষণে', 'সোমবার', 'রাজধানীর', 'বিভিন্ন', 'এলাকায়', 'জলাবদ্ধতা', 'দেখা', 'দেয়']))
# ['এলাকায়', 'ঘণ্টার', 'জলাবদ্ধতা', 'দেখা', 'দেয়', 'বিভিন্ন', 'বর্ষণে', 'ভারী', 'রাজধানীর', 'সোমবার', '১']
```

## Is any number character exists?
**INPUT:** Word \
**OUTPUT** Boolean \
**PROCESS:**  Check weather is any character numeric?\
**USE CASE:** tagging,..

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.is_number('১লা'))
# True
print(p.is_number('দেখা'))
# False
```

## Extra space remove
**INPUT:** Text \
**OUTPUT** Text \
**PROCESS:**  Remove all the extra space\
**USE CASE:** Clean text,..

```python
from sbnltk.Preprocessor import preprocessor
p=preprocessor()
print(p.extra_space_remove('  রবীন্দ্রনাথকে গুরুদেব,  কবিগুরু  ও   বিশ্বকবি অভিধায়   ভূষিত করা হয়'))
# রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়
```
