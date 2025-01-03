m,k="3243f6a8885a308d313198a2e0370734","2b7e151628aed2a6abf7158809cf4f3c"
from functools import reduce
df_mt,r_con,s_box=["02", "03", "01", "01","01", "02", "03", "01","01", "01", "02", "03","03", "01", "01", "02"],["","01000000","02000000","04000000","08000000","10000000","20000000","40000000","80000000","1b000000","36000000"],[["63","7C","77","7B","F2","6B","6F","C5","30","01","67","2B","FE","D7","AB","76"],["CA","82","C9","7D","FA","59","47","F0","AD","D4","A2","AF","9C","A4","72","C0"],["B7","FD","93","26","36","3F","F7","CC","34","A5","E5","F1","71","D8","31","15"],["04","C7","23","C3","18","96","05","9A","07","12","80","E2","EB","27","B2","75"],["09","83","2C","1A","1B","6E","5A","A0","52","3B","D6","B3","29","E3","2F","84"],["53","D1","00","ED","20","FC","B1","5B","6A","CB","BE","39","4A","4C","58","CF"],["D0","EF","AA","FB","43","4D","33","85","45","F9","02","7F","50","3C","9F","A8"],["51","A3","40","8F","92","9D","38","F5","BC","B6","DA","21","10","FF","F3","D2"],["CD","0C","13","EC","5F","97","44","17","C4","A7","7E","3D","64","5D","19","73"],["60","81","4F","DC","22","2A","90","88","46","EE","B8","14","DE","5E","0B","DB"],["E0","32","3A","0A","49","06","24","5C","C2","D3","AC","62","91","95","E4","79"],["E7","C8","37","6D","8D","D5","4E","A9","6C","56","F4","EA","65","7A","AE","08"],["BA","78","25","2E","1C","A6","B4","C6","E8","DD","74","1F","4B","BD","8B","8A"],["70","3E","B5","66","48","03","F6","0E","61","35","57","B9","86","C1","1D","9E"],["E1","F8","98","11","69","D9","8E","94","9B","1E","87","E9","CE","55","28","DF"],["8C","A1","89","0D","BF","E6","42","68","41","99","2D","0F","B0","54","BB","16"]]
def replaceS_box(rw):
    if len(rw)%2!=0:raise ValueError("len rw must mod 2 = 0")
    return "".join([s_box[int(rw[i], 16)][int(rw[i+1], 16)] for i in range(0,len(rw),2)])
def hex_xor(hex1, hex2):
    if not all(char in "0123456789ABCDEFabcdef" for char in hex1+hex2): raise ValueError("hexa invalid")
    return hex(int(hex1, 16)^int(hex2, 16))[2:].zfill(max(len(hex1), len(hex2)))
def key_expansion(key):
    if len(key)!=32:raise ValueError("length key must is 32")
    w,k,w[0],w[1],w[2],w[3]=[None]*50,[key],key[0:8],key[8:16],key[16:24],key[24:32]
    for i in range(1,11):
        w[i*4]=hex_xor(w[i*4-4],hex_xor(replaceS_box(w[i*4-1][2:8]+w[i*4-1][0:2]),r_con[i]))
        for j in range(1,4):w[i*4+j]=hex_xor(w[i*4+j-1],w[i*4-4+j])
        k.append(w[i*4]+w[i*4+1]+w[i*4+2]+w[i*4+3])
    return k,w
k,w=key_expansion(k)
def shift_rows(state=""):return "".join([state[i*2:i*2+2] for i in [0,5,10,15,4,9,14,3,8,13,2,7,12,1,6,11]])
def hex_mul(hex1,hex2):
    if not all(char in "0123456789ABCDEFabcdef" for char in hex1+hex2):raise ValueError("hexa invalid")
    mod,hex1,hex2=int("100011011",2),int(hex1,16),int(hex2,16)
    res = reduce(lambda x, y: x ^ y,(hex2 << i for i in range(hex1.bit_length()) if hex1 >> i & 1))
    while res.bit_length()>=9: res^=mod<<(res.bit_length()-9)
    return res
def mix_columns(state):
    st_mt= [state[i*2:i*2+2] for i in [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]]
    return "".join([hex(reduce(lambda x,y:x^y,[hex_mul(df_mt[i//4*4+j],st_mt[i%4+j*4]) for j in range(4)]))[2:].zfill(2) for i in [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]])
state= hex_xor(m,k[0])
for i in range(1,10):state = hex_xor(mix_columns (shift_rows(replaceS_box(state))), k[i])
print(hex_xor(shift_rows(replaceS_box(state)),k[10]))