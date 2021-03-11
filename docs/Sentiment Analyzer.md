# Sentiment Analyzer

### Model code: 
  * LR = Logistic Regression 
  * LSVC = Linear SVC
  * MNB = Multinomial naive bayes
  * RF = Random Forest
  * BERT = Bert sentiment 

## Logistic Regression
**INPUT:** model_code, sentence list \
**OUTPUT:**  1,0 prediction list, probabilistic value list   \
**PROCESS:** predict from pretrained LR model \
**USE CASE:** sentiment analysis, etc

```python
from sbnltk.SentimentAnalyzer import sentimentAnalyzer
sa=sentimentAnalyzer()
print(sa.predict('LR',['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়','সে আমার ক্লাসের খারাপ ছেলে',
                       'তিনি এই কাজটি করতে চান না','সে তার ক্লাসে সর্বোচ্চ স্কোর পায়']))

# ([1, 0, 0, 1], [0.6449975713588612, 0.45778114564313, 0.46393594035665886, 0.8066192798190904])
```

## Multinomial naive bayes
**INPUT:** model_code, sentence list \
**OUTPUT:**  1,0 prediction list, probabilistic value list   \
**PROCESS:** predict from pretrained LR model \
**USE CASE:** sentiment analysis, etc

```python
from sbnltk.SentimentAnalyzer import sentimentAnalyzer
sa=sentimentAnalyzer()
print(sa.predict('MNB',['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়','সে আমার ক্লাসের খারাপ ছেলে',
                       'তিনি এই কাজটি করতে চান না','সে তার ক্লাসে সর্বোচ্চ স্কোর পায়']))

# ([1, 1, 1, 1], [0.7662020763286507, 0.5958552168595721, 0.6210174366440201, 0.765537674170212])
```

## Linear SVC

**INPUT:** model_code, sentence list \
**OUTPUT:**  1,0 prediction list   \
**PROCESS:** predict from pretrained LR model \
**USE CASE:** sentiment analysis, etc

```python
from sbnltk.SentimentAnalyzer import sentimentAnalyzer
sa=sentimentAnalyzer()
print(sa.predict('LSVC',['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়','সে আমার ক্লাসের খারাপ ছেলে',
                       'তিনি এই কাজটি করতে চান না','সে তার ক্লাসে সর্বোচ্চ স্কোর পায়']))

# [1, 1, 0, 1]
```

## Random Forest

**INPUT:** model_code, sentence list \
**OUTPUT:**  1,0 prediction list   \
**PROCESS:** predict from pretrained LR model \
**USE CASE:** sentiment analysis, etc

```python
from sbnltk.SentimentAnalyzer import sentimentAnalyzer
sa=sentimentAnalyzer()
print(sa.predict('RF',['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়','সে আমার ক্লাসের খারাপ ছেলে',
                       'তিনি এই কাজটি করতে চান না','সে তার ক্লাসে সর্বোচ্চ স্কোর পায়']))

# ([1, 1, 1, 1], [0.7662020763286507, 0.5958552168595721, 0.6210174366440201, 0.765537674170212])
```

## BERT sentiment Analysis
**INPUT:** model_code, sentence list \
**OUTPUT:**  1,0 prediction list   \
**PROCESS:** predict from pretrained LR model \
**USE CASE:** sentiment analysis, etc

```python
from sbnltk.SentimentAnalyzer import sentimentAnalyzer
sa=sentimentAnalyzer()
print(sa.predict('BERT',['তাঁকে বাংলা ভাষার সর্বশ্রেষ্ঠ সাহিত্যিক মনে করা হয়','সে আমার ক্লাসের খারাপ ছেলে',
                       'তিনি এই কাজটি করতে চান না','সে তার ক্লাসে সর্বোচ্চ স্কোর পায়']))

# ([1, 0, 0, 1], [0.97045285, 0.8849995136260986, 0.8312564790248871, 0.96529424])
```

