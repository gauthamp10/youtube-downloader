import os
import sys 
import shutil
from pydub import AudioSegment
from pathlib import Path

def move(src, dest):
    files = [i for i in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),i)) and \
         src in i]
    
    shutil.move(files[0], dest)

def convert_mp3(vid,down_path,title):
    try:
        AudioSegment.from_file(vid).export(down_path+'Audio/'+str(title)+'.mp3', format="mp3")
        os.remove(vid)
    except Exception as e:
        print(str(e))


def check_dir():
    try:
        os_code=str(sys.platform).lower()    # get the current OS 
        if os_code=='linux':
            down_path=str(Path.home())+'/YMG/'
            AudioSegment.ffmpeg = "./ffmpeg"
            AudioSegment.ffprobe = "./ffprobe"
        
        if not os.path.exists(down_path+'/Video/' and down_path+'/Audio/'): #Creating path if not exist
            os.makedirs(down_path+'/Video/')
            print("Created")
            os.makedirs(down_path+'/Audio/')
        return down_path
        
    except Exception as e:
        print(str(e))
        return "Error!"
