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

prueba1 = s.recv(4096)

# receive message string from
# server, at a time 1024 B
try:
	msg = s.recv(4096)
except Exception:
	print("NO SE HA PODIDO DECODIFICAR")

ba.frombytes(msg)
print("Mensaje codificado: "+ str(ba))
#crc32(ba)
prueba2 = fletcher32(str(ba), len(ba))
print(prueba1.decode())
print(prueba2)
# repeat as long as message
# string are not empty

if(str(prueba1.decode()) == str(prueba2)):
	print("PRUEBA APROBADA")
else:
	print("PRUEBA DESAPROBADA")

while msg:
	print('Mensaje decodificado: ' + msg.decode())
	msg = s.recv(4096)

# disconnect the client
s.close()
