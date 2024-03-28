import bai2
pc2table = [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2, 
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
def PC2 (binKey):
    while len(binKey) < 56: binKey="0"+binKey
    binKeyAfter = ''.join([binKey[pc2table[i]-1] for i in range(48)])
    return binKeyAfter

C = bai2.C
D = bai2.D

K = []
for i in range(0,17):
    K.append(PC2(C[i]+D[i]))


for i in range(1,17):
    print("K",i,": ",K[i],sep="")