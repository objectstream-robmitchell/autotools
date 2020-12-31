from oslib_all_imports import *
from config import Config

class AutoBak:
	def __init__(self):
		self.config = Config()()
		print(self.config,type(self.config))


AutoBak()
