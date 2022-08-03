import socket
import bitarray
from CRC32 import crc32
from fletcher_checksum import fletcher32

# take the server name and port name

host = 'local host'
port = 5000

ba = bitarray.bitarray()

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect(('127.0.0.1', port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(4096)
ba.frombytes(msg)
print("Mensaje codificado: "+ str(ba))
crc32(ba)
fletcher32(str(ba), len(ba))
# repeat as long as message
# string are not empty
while msg:
	print('Mensaje decodificado: ' + msg.decode())
	msg = s.recv(4096)

# disconnect the client
s.close()
