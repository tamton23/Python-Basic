data = open('Files/data.bin', 'wb')
data.write(bytes('Hello World', 'utf-8'))
data.close()

data = open('Files/data.bin', 'rb').read()
print(data)
print(data[6: 11])


