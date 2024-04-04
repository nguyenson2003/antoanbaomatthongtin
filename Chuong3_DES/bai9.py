import bai3
import bai4
import bai5
import bai6
import bai7
import bai8

def oneRoundDES(L0,R0,K1):
    L1 = R0
    ER0 = bai5.e_box(R0)
    A = bai6.xorbit(ER0,K1)
    B = bai7.s_box(A)
    F = bai8.p_box(B)
    R1 = bai6.xorbit(L0,F)
    return L1,R1


hexatext = bai4.hexatext
L0, R0 = bai4.initial_permutation(hexatext)
L1, R1 = oneRoundDES(L0,R0,bai3.K[1])
# print("L1 =",L1)
# print("R1 =",R1)