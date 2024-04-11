import bai0
ptable = [58, 50, 42, 34, 26, 18, 10, 2, 
          60, 52, 44, 36, 28, 20, 12, 4, 
          62, 54, 46, 38, 30, 22, 14, 6, 
          64, 56, 48, 40, 32, 24, 16, 8, 
          57, 49, 41, 33, 25, 17, 9, 1, 
          59, 51, 43, 35, 27, 19, 11, 3, 
          61, 53, 45, 37, 29, 21, 13, 5, 
          63, 55, 47, 39, 31, 23, 15, 7]
def initial_permutation(hexatext):
    bintext = bin(int(hexatext,16))[2::]
    while len(bintext)<64:bintext = '0'+bintext
    bintext = ''.join([bintext[i-1] for i in ptable])
    return bintext[0:len(bintext)//2],bintext[len(bintext)//2::]

hexatext = bai0.plaintext
L0,R0 = initial_permutation(hexatext)
print("bai 4:")
print("L0 =",L0)
print("R0 =",R0)
# print(list(map(int,input().split()+input().split()+input().split()+input().split()+input().split()+input().split()+input().split()+input().split())))
