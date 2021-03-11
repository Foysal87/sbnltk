# Word Tokenizer

## Basic Word tokenizer

**INPUT:** Sentence \
**OUTPUT:** list of words \
**PROCESS:** split words \
**USE CASE:** Everywhere

```python
from sbnltk.Tokenizer import wordTokenizer,sentenceTokenizer
Wt=wordTokenizer()
print(Wt.basic_tokenizer('ভোগান্তিতে পড়েন নগরবাসী'))
# ['ভোগান্তিতে', 'পড়েন', 'নগরবাসী']
```

## Customized Word tokenizer

**INPUT:** sentence, **args \
**args:** punc=Boolean (default=True)\
            norm=Boolean (default=False) \
            dust=Boolean (default=False)
**OUTPUT:** list of words \
**PROCESS:** split sentence \
**USE CASE:** Everywhere

```python
from sbnltk.Tokenizer import wordTokenizer
Wt=wordTokenizer()
print(Wt.customized_tokenizer('রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# ['রবীন্দ্রনাথকে', 'গুরুদেব', 'কবিগুরু', 'ও', 'বিশ্বকবি', 'অভিধায়', 'ভূষিত', 'করা', 'হয়']
print(Wt.customized_tokenizer('রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',norm=True))
# ['রবিন্দ্রনাথকে', 'গুরুদেব', 'কবিগুরু', 'ও', 'বিশ্বকবি', 'অভিধায়', 'ভুষিত', 'করা', 'হয়']
print(Wt.customized_tokenizer('রবীন্দ্রনাথকেzz গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',norm=True,dust=True))
# ['রবিন্দ্রনাথকে', 'গুরুদেব', 'কবিগুরু', 'ও', 'বিশ্বকবি', 'অভিধায়', 'ভুষিত', 'করা', 'হয়']
```
# Sentence Tokenizer

## Basic Tokenizer

**INPUT:** Text \
**OUTPUT:** list of Sentences \
**PROCESS:** split text \
**USE CASE:** Everywhere

```python
from sbnltk.Tokenizer import sentenceTokenizer
sentT=sentenceTokenizer()
print(sentT.basic_tokenizer('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', ' রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়']
```

## Customized tokenizer

**INPUT:** Text, **args \
**args:** punc=Boolean (default=True)\
            norm=Boolean (default=False) \
            dust=Boolean (default=False)
**OUTPUT:** list of Sentences \
**PROCESS:** split Text \
**USE CASE:** Everywhere
```python
from sbnltk.Tokenizer import sentenceTokenizer
sentT=sentenceTokenizer()
print(sentT.customized_tokenizer('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', 'রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়']
print(sentT.customized_tokenizer('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',norm=True))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', 'রবিন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভুষিত করা হয়']
print(sentT.customized_tokenizer('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠzz (best) সাহিত্যিক মনে করা123 হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',norm=True,dust=True))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ best সাহিত্যিক মনে করা হয়', 'রবিন্দ্রনাথকে গুরুদেব কবিগুরু ও বিশ্বকবি অভিধায় ভুষিত করা হয়']
```

## Sentence Cluster
**INPUT:** Text, **args \
**args:** max_length=int (default=100) \
punc=Boolean (default=True)\
            norm=Boolean (default=False) \
            dust=Boolean (default=False)
**OUTPUT:** list of Sentences with fixed length \
**PROCESS:** split Text \
**USE CASE:** Everywhere

```python
from sbnltk.Tokenizer import sentenceTokenizer
sentT=sentenceTokenizer()
print(sentT.sentence_cluster('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।'))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', 'রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়']
print(sentT.sentence_cluster('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',max_length=50,norm=True))
# ['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা', 'হয়', 'রবিন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায়', 'ভুষিত করা হয়']
print(sentT.sentence_cluster('তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠzz (best) সাহিত্যিক মনে করা123 হয়। রবীন্দ্রনাথকে গুরুদেব, কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।',max_length=30,norm=True,dust=True))
# ['তাঁকে বাংলা ভাষার', 'সর্বশ্রেষ্ঠ best সাহিত্যিক', 'মনে করা হয়', 'রবিন্দ্রনাথকে গুরুদেব কবিগুরু', 'ও বিশ্বকবি অভিধায় ভুষিত করা', 'হয়']
```

## Vector to Text
**INPUT:** Vector, **args \
**args:** full_stop=Boolean (default=True) \
**OUTPUT:**  Text \
**PROCESS:** Make a text from sentence vector \
**USE CASE:** Everywhere

```python
from sbnltk.Tokenizer import sentenceTokenizer
sentT=sentenceTokenizer()
print(sentT.sentence_vector_to_text(['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', 'রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়']))
# তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়।রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়।
print(sentT.sentence_vector_to_text(['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়', 'রবীন্দ্রনাথকে গুরুদেব  কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়'],full_stop=False))
# তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয় রবীন্দ্রনাথকে গুরুদেব কবিগুরু ও বিশ্বকবি অভিধায় ভূষিত করা হয়
```