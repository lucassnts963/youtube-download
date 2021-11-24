import subprocess
from pytube import Playlist
from pytube import YouTube
from tqdm import tqdm

from download import Download

is_running = True

def download_video(link):
	download = Download(link)
	download.start()

def download_playlist():
	link = input('Insira o link da playlist: ')
	playlist = Playlist(link)
	for i in tqdm(range(len(playlist))):
		download_video(playlist[i])

while(is_running):
	#subprocess.run(['clear'])
	print('1 - Download de Video')
	print('2 - Download de Playlist')
	print('3 - Download de Playlist em MP3')
	print('4 - Sair')
    
	option = int(input('Informe o que deseja fazer:  '))
    
	if option == 1:
		link = input('Insira o link do video: ')
		download_video(link)
	elif option == 2:
		download_playlist()
	elif option == 3:
	  pass
	elif option == 4:
	  is_running = False
