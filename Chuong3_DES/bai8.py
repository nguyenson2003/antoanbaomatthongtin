import bai7
# print(list(map(int,input().split()+input().split()+input().split()+input().split())))
ptable = [16, 7, 20, 21, 29, 12, 28, 17, 
          1, 15, 23, 26, 5, 18, 31, 10, 
          2, 8, 24, 14, 32, 27, 3, 9, 
          19, 13, 30, 6, 22, 11, 4, 25]
def p_box(B):
    return ''.join([B[i-1] for i in ptable])

F = p_box(bai7.B)
print("bai 8:")
print("F:",F)