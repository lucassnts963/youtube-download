import os
import subprocess

from moviepy.editor import *

path = '/storage/emulated/0/projetos/youtube-download/video'

def to_mp3(file):
  if (file == 'convert.py'):
    return
  mp3 = file.replace('mp4', 'mp3')
  
  videoClip = VideoFileClip(file)
  
  audioClip = videoClip.audio
  
  audioClip.write_audiofile(mp3)
  
  audioClip.close
  videoClip.close

files = os.listdir(path)

for i in files:
  to_mp3(i)