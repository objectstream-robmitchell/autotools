from oslib_all_imports import *
from config import Config
from purge import Purge

class AutoBak:
	def __init__(self):
		self.config = Config()()
		print(self.config,type(self.config))


if __name__ == '__main__':
	TmpStorage()()
	Purge()()
	AutoBak()
