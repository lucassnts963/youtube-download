import os
from moviepy.editor import *
#video = VideoFileClip(os.path.join("path","to","movie.mp4"))
video = VideoFileClip('All of Me - John Legend - Violin and Guitar Cover - Daniel Jang.mp4')
video.audio.write_audiofile('All of Me - John Legend - Violin and Guitar Cover - Daniel Jang.mp3')