# Rezolvare Tema 4

### 1. CRC HTTP service
URL catre API-ul nostru este:
```
http://ec2-34-238-255-26.compute-1.amazonaws.com/crc
```
Testarea aplicației:
```
header = {'Content-Type': 'application/octet-stream'}
structdata = struct.pack('!IIII5s', 0x04C11DB7,0xEDB88320,0xDB710641,0x82608EDB, b'mesaj')
url = 'http://ec2-34-238-255-26.compute-1.amazonaws.com/crc'
response = requests.post(url, headers=header, data=data)
print (response.content)
```

### 2. Protocoale de routare

....
....
....
....
