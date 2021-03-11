# Extractive Summarization

## Feature Based Model
**INPUT:** Text,title(default=None),max-length(default=) \
**OUTPUT:**  text \
**PROCESS:**  generate summary based on text features \

```python
from sbnltk.Extractive_Summarizer import feature_based_model
fbm=feature_based_model()
text='''
বাংলাদেশে অবসরপ্রাপ্ত সেনা কর্মকর্তা মেজর সিনহা মো. রাশেদ খানকে পরিকল্পিতভাবে হত্যা করা হয়েছে উল্লেখ করে আজ (রোববার) আদালতে চার্জশিট জমা দেয়া হয়েছে।
হত্যাকাণ্ডের চার মাস পর আদালতে আজ এ মামলার চার্জশিট বা অভিযোগ পত্র জমা দেন র‌্যাবের তদন্তকারী কর্মকর্তা।
হত্যার আগে 'গোপন বৈঠকে টেকনাফ থানার বরখাস্তকৃত ওসি প্রদীপ কুমার তাকে হত্যার মূল পরিকল্পনা করে' বলেও তদন্তে উঠে এসেছে বলে জানায় র‌্যাব।
চার্জশিটের বিষয় নিয়ে দুপুরে রাজধানীর কারওয়ান বাজারে এক সংবাদ সম্মেলন র‍্যাবের লিগ্যাল অ্যান্ড মিডিয়া উইংয়ের পরিচালক লেফটেন্যান্ট কর্নেল আশিক বিল্লাহ এসব কথা জানিয়েছেন।
এর আগে সকালে কক্সবাজার আদালতে ২৬ পৃষ্ঠার অভিযোগপত্র জমা দেন র‍্যাবের তদন্ত কর্মকর্তা সিনিয়র সহকারী পুলিশ সুপার খায়রুল ইসলাম।
সংবাদ সম্মেলনে বলা হয়, অভিযোগ পত্রে ১৫ জনকে আসামী করা হয়েছে। এদের মধ্যে ১৪ জনকেই গ্রেফতার করা হয়েছে এবং তারা এখন কারাগারে রয়েছে।
এদের মধ্যে রয়েছেন টেকনাফ থানার বরখাস্তকৃত ওসি প্রদীপ কুমার, বাহারছড়া ক্যাম্পের বরখাস্তকৃত পরিদর্শক লিয়াকত আলী, এসআই নন্দদুলাল রক্ষিত, টেকনাফ থানার কয়েক 
জন পুলিশ সদস্য, আর্মড ব্যাটালিয়ন পুলিশের তিন সদস্য, স্থানীয় তিন বাসিন্দা, এবং বাকি একজন পলাতক। তিনি টেকনাফ থানার বরখাস্তকৃত ওসি প্রদীপ কুমারের দেহরক্ষী সাগর দেব।
কারাগারে থাকা ১৪ জনের মধ্যে ১২ জন স্বীকারোক্তিমূলক জবানবন্দী দিয়েছে।
গত ৩১শে জুলাই রাতে কক্সবাজারের একটি পুলিশ চেকপোস্টে পুলিশের গুলিতে নিহত হন অবসরপ্রাপ্ত মেজর সিনহা মোঃ রাশেদ। সেই ঘটনায় পুলিশ দুইটি মামলা করে।
'''

print(fbm.generate_summary(text))
#  বাংলাদেশে অবসরপ্রাপ্ত সেনা কর্মকর্তা মেজর সিনহা মো. রাশেদ খানকে পরিকল্পিতভাবে হত্যা করা হয়েছে উল্লেখ করে আজ (রোববার) আদালতে চার্জশিট জমা দেয়া হয়েছে।
#  এর আগে সকালে কক্সবাজার আদালতে ২৬ পৃষ্ঠার অভিযোগপত্র জমা দেন র‍্যাবের তদন্ত কর্মকর্তা সিনিয়র সহকারী পুলিশ সুপার খায়রুল ইসলাম।
#  তিনি টেকনাফ থানার বরখাস্তকৃত ওসি প্রদীপ কুমারের দেহরক্ষী সাগর দেব।
# কারাগারে থাকা ১৪ জনের মধ্যে ১২ জন স্বীকারোক্তিমূলক জবানবন্দী দিয়েছে।
#  গত ৩১শে জুলাই রাতে কক্সবাজারের একটি পুলিশ চেকপোস্টে পুলিশের গুলিতে নিহত হন অবসরপ্রাপ্ত মেজর সিনহা মোঃ রাশেদ।

print(fbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র'))
print(fbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র', max_length=4))
```

##  word2vec_based_model
**INPUT:** Text,title(default=None),max-length(default=5) \
**OUTPUT:**  text \
**PROCESS:**  generate summary based on text context \
```python
from sbnltk.Extractive_Summarizer import word2vec_based_model
w2vbm=word2vec_based_model()
text=''' Given Text '''
print(w2vbm.generate_summary(text))
print(w2vbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র'))
print(w2vbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র', max_length=4))
```

## transformer_based_model
**INPUT:** Text,title(default=None),max-length(default=5) \
**OUTPUT:**  text \
**PROCESS:**  generate summary based on Semantic similarity \

```python
from sbnltk.Extractive_Summarizer import transformer_based_model
tbm=transformer_based_model()
text=''' Given Text '''
print(tbm.generate_summary(text))
print(tbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র'))
print(tbm.generate_summary(text,title='মেজর সিনহা হত্যার অভিযোগ পত্র', max_length=4))
```

