import bai0
def PC1 (hexaKey):
    pc1table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 
                10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
                63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 
                14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    binKey = bin(int(hexaKey,16))[2::]
    while len(binKey) < 64: binKey="0"+binKey
    binKeyAfter = ''.join([binKey[pc1table[i]-1] for i in range(56)])
    return [binKeyAfter[0:28],binKeyAfter[28:56]]

# plainkey="F35D514714F45A8A"
plainkey = bai0.key
pc1 = PC1(plainkey)
print("bai 1:")
print("C0: ",pc1[0],"D0: ",pc1[1])
