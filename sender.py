import socket
import bitarray
import numpy as np
from fletcher_checksum import fletcher32
from CRC32 import crc32
import random

def ruido(msg):
	ruido = True
	noRuido = False
	a = np.random.choice([ruido,noRuido], size=1, p=[1,0])
	print(a)
	if True in a:
		print("RUIDO")
		i = random.randint(0, len(msg) -1)
		if msg[i] == 0:
			msg[i] = 1
		else:
			msg[i] = 0
	else:
		print("NO RUIDO")
	


# take the server name and port name
host = 'local host'
port = 5000
ba = bitarray.bitarray()

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
c, addr = s.accept()

# display client address
print("CONNECTION FROM:", str(addr))

# send message to the client after
# encoding into binary string
msg = input("INGRESE EL MENSAJE: \n")
ba.frombytes(msg.encode('utf-8'))


print(ba)
ruido(ba)
c.send(ba)

#Receiver
#bitarray.bitarray(ba).tobytes().decode('utf-8')


# disconnect the server
c.close()
