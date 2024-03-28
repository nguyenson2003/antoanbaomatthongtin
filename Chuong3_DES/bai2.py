import bai1
tableLeftShift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
def shift(binKeyAfter,shiftKey):
    return binKeyAfter[shiftKey::]+binKeyAfter[0:shiftKey]

# print(bai1.pc1[0][1])
pc1=bai1.pc1
C = [pc1[0]]
D = [pc1[1]]
for i in range(16):
    C.append(shift(C[i-1+1],tableLeftShift[i]) )
    D.append(shift(D[i-1+1],tableLeftShift[i]) )

# for i in range(17):
#     print("C",i,": ",C[i],sep="",end=", ")
#     print("D",i,": ",D[i],sep="")