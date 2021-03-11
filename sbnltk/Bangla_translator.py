'''
We used Google translator here.
google_trans_new python package.
We use 2 seconds delay for large data in google translator
We use autodetect for large translator call
'''
import time
from time import time
from sbnltk import sbnltk_default
from google_trans_new import google_translator
translator = google_translator()

class bangla_google_translator():

    def __init__(self):
        try:
            file=open(sbnltk_default.sbnltk_root_path+'dataset/auto_detect_large_translate.txt','w')
            file.write(str(str(0.0)+' '+'0'))
        except:
            print(f"{sbnltk_default.bcolors.FAIL}ERROR 101: Error in auto detecting text file initializing!! {sbnltk_default.bcolors.ENDC}")


    def translate_E2B(self,sentence):
        try:
            with open(sbnltk_default.sbnltk_root_path+'dataset/auto_detect_large_translate.txt','r') as f:
                line=f.readline()
                item=line.split(' ')
                last_epoch = float(item[0])
                epoch_count=int(item[1])
            now=float(time())
            if now-last_epoch<1.0 and epoch_count>500:
                time.sleep(2)
            if now-last_epoch>1000.0:
                epoch_count=0
            epoch_count+=1
            translation=translator.translate(sentence,lang_tgt='bn')
            now=float(time())
            with open(sbnltk_default.sbnltk_root_path+'dataset/auto_detect_large_translate.txt','w') as f:
                f.write(str(str(now)+' '+str(epoch_count)))
                f.close()
            return translation
        except:
            print(f"{sbnltk_default.bcolors.FAIL}ERROR 102: Error in E2B translation!! Check connection{sbnltk_default.bcolors.ENDC}")
            return sentence

    def translate_B2E(self,sentence):
        try:
            with open(sbnltk_default.sbnltk_root_path+'dataset/auto_detect_large_translate.txt','r') as f:
                line=f.readline()
                item=line.split(' ')
                last_epoch = float(item[0])
                epoch_count=int(item[1])
            now=float(time())
            if now-last_epoch<1.0 and epoch_count>500:
                time.sleep(2)
            if now-last_epoch>1000.0:
                epoch_count=0
            epoch_count+=1
            translation=translator.translate(sentence,lang_tgt='en')
            now=float(time())
            with open(sbnltk_default.sbnltk_root_path+'dataset/auto_detect_large_translate.txt','w') as f:
                f.write(str(str(now)+' '+str(epoch_count)))
                f.close()
            return translation
        except:
            print(f"{sbnltk_default.bcolors.FAIL}ERROR 103: Error in B2E translation!! Check connection{sbnltk_default.bcolors.ENDC}")
            return sentence

