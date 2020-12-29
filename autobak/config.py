from oslib_all_imports import *

class Config:
	def __init__(self):
		self.aesutil = AESUtil(os.getenv('AESKEY'))
		self.config = self._get_config()

	def __call__(self):
		return self.config

	def _get_config(self):
		ciphertext = IO.get_resource('https://www.objectstream.com/autobak/'+hostname)
		return json.loads(self.aesutil.decrypt(ciphertext).decode())

print( Config()() ) 
