import os

def run(**args):

	print "[*] w module dirlister."
	files = os.listdir(".")

	return str(files)
