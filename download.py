from pytube import YouTube
from tqdm import tqdm

class Download:
	link = ''
	youtube = None
	title = ''
	filesize = 0
	previous_size = 0
	progress_bar = None

	def __init__(self, link):
		self.youtube = YouTube(link)
		self.filesize = self.youtube.streams.get_highest_resolution().filesize
		self.youtube.register_on_progress_callback(self.on_progress)
		self.youtube.register_on_complete_callback(self.on_complete)

	def start(self):
		self.progress_bar = tqdm(total=self.filesize, unit='iB', colour='red', unit_scale=True)
		self.youtube.streams.get_highest_resolution().download()
		print('start()')

	def on_progress(self, chunk, fh, bytes_remaining):
		downloaded = self.filesize - bytes_remaining
		update = downloaded - self.previous_size
		self.previous_size = downloaded
		self.progress_bar.update(update)
		#print('Baixando... {}/{}'.format(bytes_remaining, self.filesize))

	def on_complete(self, streams, file_path):
		self.progress_bar.close()
		self.progress_bar = None
		print('Download Completo. Salvo em {}.'.format(file_path))

	