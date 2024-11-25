import os
import uuid
import base64
import json

class Ju():
	def __init__(self, path):
		self.path = path
		self.files = os.listdir(self.path)

	def rename(self):
		# avoid same file name
		for i, f in enumerate(self.files):
			id = uuid.uuid4()
			os.rename(f'{self.path}/{f}', f'{self.path}/{id}.jpg')

		self.files = os.listdir(self.path)
		# rename 
		for i, f in enumerate(self.files):
			os.rename(f'{self.path}/{f}', f'{self.path}/{i+1}.jpg')
		
		self.files = os.listdir(self.path)
	
	def getBase64(self, filename=''):
		ret = []
		if filename == '':
			for f in self.files:
				with open(f'{self.path}/{f}', 'rb') as img:
					ret.append(base64.b64encode(img.read()))
		else:
			with open(f'{self.path}/{filename}', 'rb') as img:
				ret.append(base64.b64encode(img.read()))

		return ret

ju = Ju('./public/aju')