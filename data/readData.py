# python 3.7

import shelve
import os

DATA_PATH = "data"

def checkFileExist(fileURI):
	if os.path.isfile(fileURI):
		return True
	return False

with shelve.open(DATA_PATH) as read:
	keys = list(read.keys())
	for key in keys:
		print(key)