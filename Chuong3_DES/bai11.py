import bai10

reverseIPtable=[40, 8, 48, 16, 56, 24, 64, 32, 
                39, 7, 47, 15, 55, 23, 63, 31, 
                38, 6, 46, 14, 54, 22, 62, 30, 
                37, 5, 45, 13, 53, 21, 61, 29, 
                36, 4, 44, 12, 52, 20, 60, 28, 
                35, 3, 43, 11, 51, 19, 59, 27, 
                34, 2, 42, 10, 50, 18, 58, 26, 
                33, 1, 41, 9, 49, 17, 57, 25]
# print(list(map(int,input().split()+input().split()+input().split()+input().split()+input().split()+input().split()+input().split()+input().split())))
def reverse_initial_permutation(L16,R16):
    bintext = R16+L16
    bintext = ''.join([bintext[i-1] for i in reverseIPtable])
    return bintext

C = reverse_initial_permutation(bai10.L[16],bai10.R[16])
print("bai 11:")
print(C)
print(hex(int(C,2))[2::].upper())