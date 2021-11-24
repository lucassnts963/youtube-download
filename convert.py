import subprocess
import os

from moviepy.editor import *

class Mp3:
  title = ''
  
  def __init__(self, title):
    self.title = title.rstrip().lstrip()
    
  def convert(self):
    videoClip = VideoFileClip(self.title + '.mp4')
    audioClip = videoClip.audio
    
    audioClip.write_audiofile(self.title + '.mp3')
    
    audioClip.close()
    videoClip.close()
    self.move_file('video', self.title + '.mp4')
    self.move_file('audio', self.title + '.mp3')
  
  def move_file(self, folder, file):
	  subprocess.run(['mv', file, folder])
	   
	def convert_all(self):
	  path ='/storage/emulated/0/projetos/youtube-download/video'
	  files = os.listfile(path)
	  print(files)