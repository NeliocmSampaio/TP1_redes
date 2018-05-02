import socket
import sys
import math

def connect( tcp ):
	op = sys.argv[1]

	tcp[0] = socket.socket ( socket.AF_INET, socket.SOCK_STREAM, 0)

	if( op == '-s'):
		HOST = ''
		PORT = int( sys.argv[2] )

		ORIG = (HOST, PORT)
		tcp[0].bind( ORIG )
		tcp[0].listen(1)
		connection, client = tcp[0].accept()

		print("Connection established")
	else:
		h, p = sys.argv[2].split(':')
		HOST = h
		PORT = int( p )

		DEST = (HOST, PORT)
		tcp[0].connect( DEST )

		print("connection established")

def disconnect( tcp ):
	tcp[0].close()

	print("Connection closed")

def hex1(x):
	if x<10:
		return str(x)
	else:
		return chr( ord('A') + (x-10) )

def hext(x, t):
	print ('x=', x)
	if x<10:
		a = str(x)
	else:
		a = chr( ord('A') + (x-10) )

	r = ''
	for i in range( t-len(a) ):
		r += '0'
	r += a

	print( r )
	return r

def encodechar(c):
	r = hex1( (c&240)>>4 ) 	#10'240 = b'11110000
	r += hex1( (c&15) )		#10'15 = b'00001111
	return r 

def encode16(x, t):
	aux = ''
	for i in range( len(x) ):
		#print( x[i], "len: ", len(x))
		if x[i]=='\n':
			break
		aux += encodechar( ord( x[i] ) )
	
	return aux

#Transforma um inteiro em uma string de tamanho t. Coloca
#'0' à esquerda para completar o tamanho. 't' em nibbles.
def strise( x, t ):
	aux = str( x )
	r = ''
	for i in range( t-len(aux) ):
		r += '0'
	r += aux
	return r

# a e b strings de dois chars (dois bytes).
def shortsum(a, b):
	x = ord( a[1] )
	x += ord( a[0] ) << 8
	y = ord( b[1] )
	y += ord( b[0] ) << 8
	
	#print(x)
	#print(y)

	r = x+y
	mask = 65536	# 10'65536 == 2'10000000000000000

	while r&mask != 0:
		r = r&65535		# 10'65535 == 2'1111111111111111
		r += 1
	return r

def checksum(x):
	#print(x)
	sum = 0
	for i in range( len(x) ):
		if i%2==0 :
			aux = ''
			#print(i, " ", len(x))
			aux = x[i]
			if i+1<len(x):
				aux += x[i+1]
			else:
				aux += '0'

			#print("aux: ", aux)

			# 10'65280 == b'1111111100000000
			s = ( chr( (sum&65280)>>8 ) ) + ( chr(sum&255) )

			#print( aux )
			#print( s )

			sum = shortsum( s, aux )
	#print( "sum: ", sum )
	return sum

def format(x):
	if x=='a':
		return 'A'
	else:
		if x=='b':
			return 'B'
		else:
			if x=='c':
				return 'C'
			else:
				if x=='d':
					return 'D'
				else:
					if x=='e':
						return 'E'
					else:
						if x=='f':
							return 'F'
						#else:
	return x

def itohex(x):
	#print( type(x), ": ", x)
	#print( hex(43781) )
	aux = hex(x)
	#print(aux)
	r = ''
	for i in range(len( aux )):
		if aux[i]=='x':
			index = i+1
			break
	for i in range(index, len(aux)):
		#print( type(aux[i]) )
		r += format( aux[i])

	return r

def encode(x, id):
	r = 'dcc023c2dcc023c2'
	#print( hex	(len(x)) )
	#print("ito: ", itohex(len(x) ) )
	#r += hext( len(x), 4 )
	r += itohex( len(x) )
	r += '000000'
	r += encode16( x, 4)
	#print("x: ", x, "enc: ", encode16(x, 4))
	print("NO checksum:", r)

	cks = itohex( checksum(r) )
	print( "cks: ", cks )

	r = 'dcc023c2dcc023c2'
	#print( hex	(len(x)) )
	r += itohex( len(x) )
	r += cks
	r += '00'
	r += encode16( x, 4)

	print( r )

	return r

# Divide uma string em array de len(s)/t posições.
def dividestr(s, t):
	r = []
	for i in range( math.ceil( len(s)/t ) ):
		r.append('')

	for i in range( len(s) ):
		index = math.ceil( (i+1)/t ) -1
		#print(index)
		r[ index ] += s[i]
	return r

def send(fileName):
	ID = 0
	f = open( fileName, 'r')

	text = f.readlines()
	for line in text:
		l = dividestr( line, 65535 )	#10'65535 == 16'FFFF
		print("line: ", l)
		for i in l:
			msg = encode(i, ID)
			ID += 1
			#print(msg)

	f.close()

send(sys.argv[3])


	
#tcp = [0]
#connect( tcp )



#disconnect( tcp )

