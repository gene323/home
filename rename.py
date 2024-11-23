import os
import uuid

path = 'public/aju'
fs = os.listdir(path)

# avoid same file name
for i, f in enumerate(fs):
	id = uuid.uuid4()
	os.rename(f'{path}/{f}', f'{path}/{id}.jpg')

fs = os.listdir(path)
# rename 
for i, f in enumerate(fs):
	os.rename(f'{path}/{f}', f'{path}/{i+1}.jpg')