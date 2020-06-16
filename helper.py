import requests
from pytube import YouTube
import moviepy.editor as mp
import os
import datetime 
import time

#HELPER METHODS

def retrieve_title(url):
    
    try:
        streams = YouTube(url)
    except:
        return "Error Occurred"
    else:
        audio_path = (streams.streams.filter(file_extension='mp4', only_audio = True)[0]).download(filename = 'audio')
        return streams.title

def retrieve_length(url):
 
    streams = YouTube(url)
    return str(datetime.timedelta(seconds = streams.length))

def retrieve_thumbnail(url):
    
    streams = YouTube(url)
    return streams.thumbnail_url

def download(title):
    
    output_path = os.getcwd()
    mp3_path = os.path.join(output_path, '{}.mp3'.format(title))
    audio_path = os.path.join(output_path, 'audio.mp4')
    
    if os.path.isfile(mp3_path):
        return
    
    clip = mp.AudioFileClip(audio_path)
    clip.write_audiofile(mp3_path)

def remove(title):
    os.remove(os.path.join(os.getcwd(), "audio.mp4"))
    time.sleep(600)
    os.remove(os.path.join(os.getcwd(), "{}.mp3".format(title)))