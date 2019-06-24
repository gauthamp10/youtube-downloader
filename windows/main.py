from __future__ import unicode_literals
from pydub import AudioSegment
from sys_sys import *
import youtube_dl
import wget
import eel

 

options = {            #default non chrome options
    'mode': '--app',
    'host': 'localhost',
    'port': 8033,
}



eel.init('web')


@eel.expose
def get_info(URL,av):
    try:
        with youtube_dl.YoutubeDL() as ydl:
            info=ydl.extract_info(URL,download=False)
            alert={"title":info['title'],"video_id":info['id'],"thumb":info['thumbnail'],"url":URL,"av":av}
            return alert
    except Exception as e:
        print(str(e))
        return("Error!")
    
        
@eel.expose
def download(URL,av):
    try:
        if av=="mp3":
            ydl_options = {
                'format': 'bestaudio/best',
                'extractaudio' : True,  # only keep the audio
                'outtmpl': '%(id)s',    # name the file the ID of the video
                'noplaylist' : True,    # only download single song, not playlist
            }
        
        else:
            ydl_options = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(id)s',    # name the file the ID of the video
                'noplaylist' : True,    # only download single song, not playlist
            }

        down_path=check_dir()
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info=ydl.extract_info(URL)
            vid=info['id']
            title=info['title']
            thumb=info['thumbnail']

        if av=='mp4':
            move(vid,down_path+'Video/'+str(title))
        else:
            convert_mp3(vid,down_path,title)
        if av=='mp3':
            down_path=down_path+"Audio/"
        else:
            down_path=down_path+"Video/"    
            
        alert={"title":title,"thumb":thumb,"path":down_path}
        return alert
    except Exception as e:
        print(str(e))
        return("Error!")



def eel_repeat(options):
    try:
        eel.start('test.html')
    except Exception as e:
        print("Exception:",str(e))
        try:
            eel.start('test.html',options =options)
        except Exception as e:
            print("Exception:",str(e))
            pass


eel_repeat(options)  # Repeating the function call backs synchronous



