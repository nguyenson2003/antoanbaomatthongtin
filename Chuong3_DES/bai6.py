import bai5
import bai3
def xorbit(ER0,K1):
    return ''.join([chr(ord(i)^ord(j)^ord('0')) for i,j in zip(ER0,K1)])
A = xorbit(bai5.ER0,bai3.K[1])
print("bai 6:")
print("A:",A)