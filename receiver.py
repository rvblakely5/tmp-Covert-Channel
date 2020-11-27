import os
import os.path
from os import path

char = ""
bit = 0
drd = "/tmp/DRD"

while True:
	#If the character flag is set, decode
	if path.exists("/tmp/CHR"):
		letter = "".join([chr(int(binary, 2)) for binary in char.split(" ")])
		if len(char) == 7:
			print(char + " | " + letter)
		else:
			print(char + "  | " + letter)
		char = ""
		os.remove("/tmp/CHR")
	#Check data set ready
	if path.exists("/tmp/DSR"):
		#Check DATA
		if path.exists("/tmp/DATA"):
			char += "1"
		else:
			char += "0"
		#Set data read
		open(drd, 'a').close()
		#Delete data set ready
		os.remove("/tmp/DSR")
		#Delete DATA entry
		if path.exists("/tmp/DATA"):
			os.remove("/tmp/DATA")



