import bai3
import bai9

L = [None]*17
R = [None]*17
L[0]=bai9.L0
R[0]=bai9.R0
for i in range(1,17):
    L[i],R[i] = bai9.oneRoundDES(L[i-1],R[i-1],bai3.K[i])

# for i in range(0,17):
#     print(f"L{i} = {L[i]}, R{i} = {R[i]}")