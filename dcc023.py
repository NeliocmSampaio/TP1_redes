import socket
import sys

op = sys.argv[1]
if( op == "-s" ):
	HOST = ''
	PORT = int( sys.argv[2] )
else:
	HOST, PORT = sys.argv[2].split(':')

print(op," ",HOST," ", PORT)
tcp = socket.socket( socket.AF_INET, socket.SOCK_STREAM, 0 )

def server():
	orig = (HOST, PORT)
	tcp.bind(orig)
	tcp.listen(1)
	con, cliente = tcp.accept()

def client():
	dest = (HOST, PORT)
	tcp.connect( dest )

	msg = "voiala"
	tcp.send( msg.encode('ascii') )

if(op=="-s"):
	server();
else:
	client();

tcp.close()