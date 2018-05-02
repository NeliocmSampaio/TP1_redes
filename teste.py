'''
def hex(x):
	if x<10:
		return str(x)
	else:
		return chr( ord('A') + (x-10) )

def encodechar(c):
	r = hex( (c&240)>>4 )
	r += hex( (c&15) )
	print(r, " ", len(r))
	return r 

def encode16(s, t):
	r = ''
	for i in range( len(s) ):
		r += encodechar( ord( s[i] ) )
	return r


print( encode16( 'abcdefghijklmnopqrstuvwxyz', 8 ) )

def readFile( fileName ):
	arq = open(fileName, 'r')
	texto = arq.readlines()
	for linha in texto:
		print(linha)
	arq.close()

'''

def hex1(x):
	if x<10:
		return str(x)
	else:
		return chr( ord('A') + (x-10) )

def encodechar(c):
	r = hex1( (c&240)>>4 ) 	#10'240 = b'11110000
	r += hex1( (c&15) )		#10'15 = b'00001111
	return r 

def encode16(x, t):
	aux = ''
	for i in range( len(x) ):
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
	sum = 0
	for i in range( len(x) ):
		if i%2==0 :
			aux = ''
			aux = x[i]+x[i+1]

			# 10'65280 == b'1111111100000000
			s = ( chr( (sum&65280)>>8 ) ) + ( chr(sum&255) )

			#print( aux )
			#print( s )

			sum = shortsum( s, aux )
	#print( sum )
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
	print(aux)
	r = ''
	for i in range(len( aux )):
		if aux[i]=='x':
			index = i+1
			break
	for i in range(index, len(aux)):
		print( type(aux[i]) )
		r += format( aux[i])

	return r

save = checksum('dcc023c2dcc023c2000F000000313332333333343335333633373338')
#print( hex(43781) )
print(itohex( 65535 ))
#print( shortsum('ab', 'ab') )

'''
a = chr( 128 )
b = chr( 0 )
c = chr( 128 )
d = chr( 0 )
shortsum( a+b, c+d )
'''

'''
s = ''
for i in range( 10, 20 ):
	s += chr( i )

a = 'dcc023c2dcc023c2'
a += strise( len( s ), 4 )
a += '0000'
a += '00'
a += strise( s, 4 )

print( a )
print("codificado:")
print( encode16(a, 4) )
'''