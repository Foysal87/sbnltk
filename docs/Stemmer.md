# STEMMER


## Stem a word

**INPUT:** Word \
**OUTPUT:** Word \
**PROCESS:** Remove suffix from Word \
**USE CASE:** Clean Text, Frequency count, Searching algorithm,
so on...

```python
from sbnltk.Stemmer import stemmerOP
st=stemmerOP()
print(st.stemWord('রবীন্দ্রনাথকে'))
# রবীন্দ্রনাথ
```

## Stem a Sentence

**INPUT:** Sentence \
**OUTPUT:** Sentence \
**PROCESS:** Remove suffix from Sentence \
**USE CASE:** Clean Text, Frequency count, Searching algorithm,
so on...

```python
from sbnltk.Stemmer import stemmerOP
st=stemmerOP()
print(st.stemSent('ভোগান্তিতে পড়েন নগরবাসী'))
# ভোগান্তি পড় নগরবাসী
```
