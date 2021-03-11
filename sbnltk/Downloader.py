import gdown
import os
from sbnltk import sbnltk_default
from os import path

class downloader():
    __root_path = sbnltk_default.sbnltk_root_path
    download_link={}            # for reserved link
    download_link_default="142XvJg9xdpgzuYD31Y4pm-ZVdMaWmtuq"    # deafault download link
    url_prefix="https://drive.google.com/uc?id="    # download url prefix


    def __init__(self):
        try:
            #dataset and model directory create
            if path.exists(self.__root_path+'dataset')==False:
                os.mkdir(self.__root_path+'dataset')
            if path.exists(self.__root_path+'model')==False:
                os.mkdir(self.__root_path+'model')

            #download link download if it is not exist
            if path.exists(self.__root_path+'dataset/download_link.txt')==False:
                url = self.url_prefix+self.download_link_default;
                output = self.__root_path+'dataset/download_link.txt'
                gdown.download(url, output, quiet=False)

            # mapping download link
            for line in open(self.__root_path+'dataset/download_link.txt','r'):
                line=line.rstrip('\n')
                items=line.split(' ')
                self.download_link[items[0]]=(items[1],items[2])    # Header = (download_id, fileType)
        except:
            raise ValueError("Error in loading download link! Check Internet connection And Try again!")

    '''
    model_path='model/'     for models
    model_path='dataset/'   for dataset
    '''

    def download(self,model,model_path):
        try:
            if self.download_link.get(model)==None:
                raise ValueError('Model Name does not exists!! ')

            model_path=model_path+model+'.'+self.download_link[model][1]
            if path.exists(model_path)==True:
                pass
            else:
                url = self.url_prefix + self.download_link[model][0]
                output = model_path
                gdown.download(url, output, quiet=False)
        except:
            raise ValueError("Error when downloading model!! Check internet Connection!!")

    def remove(self,model_path):
        try:
            os.remove(model_path)
            print(f"{sbnltk_default.bcolors.OKGREEN} {model_path} is removed!! {sbnltk_default.bcolors.ENDC} ")
        except:
            raise  ValueError("Model path does not exist!!")


    def reDownload(self,model,model_path):
        try:
            if self.download_link.get(model)==None:
                raise ValueError("Model path does not exist!!")
            model_path=model_path+model+'.'+self.download_link[model][1]
            if path.exists(model_path)==True:
                self.remove(model_path)
            url = self.url_prefix + self.download_link[model][0]
            output = model_path
            gdown.download(url, output, quiet=False)
            print(f"{sbnltk_default.bcolors.OKGREEN} Download Completed!! {sbnltk_default.bcolors.ENDC} ")
        except:
            raise ValueError("Error when downloading model!! Check Internet Connection")
