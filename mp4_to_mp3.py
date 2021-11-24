from moviepy.editor import *

mp4 = 'Video.mp4'

mp3 = 'audio.mp3'

videoClip = VideoFileClip(mp4)

audioClip = videoClip.audio

audioClip.write_audiofile(mp3)

audioClip.close()
videoClip.close()

