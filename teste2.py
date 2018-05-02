def carry_around_add(a, b):
    c = a + b
    return(c &0xffff)+(c >>16)

def checksum(msg):
    s =0
    for i in range(0, len(msg),2):
        w =(msg[i])+((msg[i+1])<<8)
        s = carry_around_add(s, w)
    return~s &0xffff


print( checksum('dcc023c2dcc023c2000F000000313332333333343335333633373338') )