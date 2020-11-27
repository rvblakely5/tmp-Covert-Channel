import sys
import os
import os.path
from os import path
import time

#Flag file paths
dpath = "/tmp/DATA"
dsr = "/tmp/DSR"
drd = "/tmp/DRD"

#Secret message from command line
secret = sys.argv[1]

#Binary encode secret message
sec_bin = ' '.join(format(ord(x), 'b') for x in secret)
sec_bin += ' '

#Empty out potential leftover flag files
if path.exists(drd):
	os.remove(drd)
if path.exists(dsr):
	os.remove(dsr)
if path.exists(dpath):
	os.remove(dpath)

for bit in sec_bin:
	#If character is complete signal to decode
	#Accounts for 6-bit characters
	if bit == ' ':
		open('/tmp/CHR', 'a').close()
	else:
		#Check if data ready, otherwise pause
		if path.exists("/tmp/DRD") == False:
			time.sleep(0.1)
		#If bit is 1, create /tmp/DATA
		if bit == "1":
			open(dpath, 'a').close()
		#Set data set ready file
		open(dsr, 'a').close()
		#Pause for 0.1 seconds
		time.sleep(0.001)

