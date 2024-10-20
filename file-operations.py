def newfile():
	f = open('Files/data.txt', 'w')
	f.write('hello\n')
	f.write('world\n')
	f.close()

def readfile():
	f = open('Files/data.txt')
	text = f.read()
	print(text)
	print(text.split())
	f.close()

newfile()
readfile()
