from oslib_all_imports import *

class Purge:
	def __init__(self,config):
		self.config = config

	def __call__(self):
		for config in self.config:
			print(config['s3bucket'], config['backup_prefix'],str(config['keep']))




'''
[{'id': 'workstation-developement-entry', 'host': 'workstation.okc.objectstream.com', 'type': 'tar_filesystem_hot', 'keep': 10, 'location': '/etc/nginx', 'backup_prefix': 'autobck.workstation.nginx', 's3bucket': 'tmp1.objectstream.com', 'tmpdir': '/var/tmp'}] <class 'list'>
'''
