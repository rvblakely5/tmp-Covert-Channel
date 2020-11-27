# tmp-Covert-Channel
Interprocess covert channel over /TMP

/tmp Covert Channel

Requirements:
	-Python2

Instructions:

Run receiver.py and leave running while waiting for a transmission from the sender.

Run sender.py with your message of chosing specified after in quotations " ".

Example Usage/Output:
```
	Sender: 
		tmp % python sender.py "Hell0 w0rld th15 is my m3ss4ge"

	Receiver:
		tmp % python receiver.py
		1001000 | H
		1100101 | e
		1101100 | l
		1101100 | l
		110000  | 0
		100000  |  
		1110111 | w
		110000  | 0
		1110010 | r
		1101100 | l
		1100100 | d
		100000  |  
		1110100 | t
		1101000 | h
		110001  | 1
		110101  | 5
		100000  |  
		1101001 | i
		1110011 | s
		100000  |  
		1101101 | m
		1111001 | y
		100000  |  
		1101101 | m
		110011  | 3
		1110011 | s
		1110011 | s
		110100  | 4
		1100111 | g
		1100101 | e
```
