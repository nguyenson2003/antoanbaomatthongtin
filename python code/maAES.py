# tạo mảng Rcon, để phù Rcon[1]="01" thì ta tạo thêm 1 phần tử rỗng 
r_con=["","01000000","02000000","04000000","08000000",
       "10000000","20000000","40000000","80000000","1b000000","36000000"]
#tạo mảng S-box
s_box=[["63","7C","77","7B","F2","6B","6F","C5","30","01","67","2B","FE","D7","AB","76"],
       ["CA","82","C9","7D","FA","59","47","F0","AD","D4","A2","AF","9C","A4","72","C0"],
       ["B7","FD","93","26","36","3F","F7","CC","34","A5","E5","F1","71","D8","31","15"],
       ["04","C7","23","C3","18","96","05","9A","07","12","80","E2","EB","27","B2","75"],
       ["09","83","2C","1A","1B","6E","5A","A0","52","3B","D6","B3","29","E3","2F","84"],
       ["53","D1","00","ED","20","FC","B1","5B","6A","CB","BE","39","4A","4C","58","CF"],
       ["D0","EF","AA","FB","43","4D","33","85","45","F9","02","7F","50","3C","9F","A8"],
       ["51","A3","40","8F","92","9D","38","F5","BC","B6","DA","21","10","FF","F3","D2"],
       ["CD","0C","13","EC","5F","97","44","17","C4","A7","7E","3D","64","5D","19","73"],
       ["60","81","4F","DC","22","2A","90","88","46","EE","B8","14","DE","5E","0B","DB"],
       ["E0","32","3A","0A","49","06","24","5C","C2","D3","AC","62","91","95","E4","79"],
       ["E7","C8","37","6D","8D","D5","4E","A9","6C","56","F4","EA","65","7A","AE","08"],
       ["BA","78","25","2E","1C","A6","B4","C6","E8","DD","74","1F","4B","BD","8B","8A"],
       ["70","3E","B5","66","48","03","F6","0E","61","35","57","B9","86","C1","1D","9E"],
       ["E1","F8","98","11","69","D9","8E","94","9B","1E","87","E9","CE","55","28","DF"],
       ["8C","A1","89","0D","BF","E6","42","68","41","99","2D","0F","B0","54","BB","16"]
       ]
#theo đầu bài thì key là ...
# k="CDAB0FC51CACBCF9A8A348C3D2D0247A"

#hàm chia khóa k thành 4 phần
def div_k_into_4_word(k):
    if len(k)!=32:
        raise ValueError("len k must is 32")
    #lấy trong k từ vị trí 0 đến 7
    w0=k[0:8]
    w1=k[8:16]
    w2=k[16:24]
    w3=k[24:32]
    return w0,w1,w2,w3
# hàm dịch vòng trái 1byte
def RotWord(w3):
    if len(w3)!=8:
        raise ValueError("len w3 must is 8")
    b0=w3[0:2]
    return w3[2:8]+w3[0:2]
#hàm thay thế rw bằng từ trong S-box
def replaceS_box(rw):
    if len(rw)%2!=0:
        raise ValueError("len rw must mod = 0")
    i=0
    res=""
    while i<len(rw):
        #chuyển rw thứ i từ hệ cơ số 16 về hệ cơ số 10
        row=int(rw[i], 16)
        col=int(rw[i+1], 16)
        res+=s_box[row][col]
        i+=2
    return res

# tạo function xor hexa
def hex_xor(hex1, hex2):
    if not all(char in "0123456789ABCDEFabcdef" for char in hex1+hex2):
        raise ValueError("hexa invalid")
    return hex(int(hex1, 16)^int(hex2, 16))[2:].zfill(max(len(hex1), len(hex2)))

#
#k ví dụ của thầy
key="2b7e151628aed2a6abf7158809cf4f3c"
#m là plaintext
m="3243f6a8885a308d313198a2e0370734"
#mảng w
w=[None]*50
#Chia khóa K (128 bit) thành 4 word (32 bit)
w[0],w[1],w[2],w[3]=div_k_into_4_word(key)
#Dịch vòng trái 1 byte đối với w3 (32 bit)
rw=RotWord(w[3])
#Thay thế từng byte trong rw bằng bảng S-box SubWord
sw=replaceS_box(rw)
#sw XORbit với Rcon[j]
xcsw=hex_xor(sw,r_con[1])
#Tính khóa K1 = (w4, w5, w6, w7)
w[4]=hex_xor(w[0],xcsw)
w[5]=hex_xor(w[4],w[1])
w[6]=hex_xor(w[5],w[2])
w[7]=hex_xor(w[6],w[3])

#mảng k
k=[w[0]+w[1]+w[2]+w[3]]
k.append(w[4]+w[5]+w[6]+w[7])
#LẶP LẠI từ Bài 2 đến Bài 5 để tạo các khóa K2, K3, ..., K10
for i in range(2,11):
    rw=RotWord(w[i*4-1])
    sw=replaceS_box(rw)
    xcsw=hex_xor(sw,r_con[i])
    w[i*4]=hex_xor(w[i*4-4],xcsw)
    w[i*4+1]=hex_xor(w[i*4],w[i*4-3])
    w[i*4+2]=hex_xor(w[i*4+1],w[i*4-2])
    w[i*4+3]=hex_xor(w[i*4+2],w[i*4-1])
    k.append(w[i*4]+w[i*4+1]+w[i*4+2]+w[i*4+3])
# nếu w43=b6630ca6 thì đã sinh 10 khóa thành công 



#hàm addroundkey thực chất là xor_hexa
def AddRoundKey(hex1, hex2):
    return hex_xor(hex1,hex2)

#mảng dịch vòng trái 0,5,10,15,4,9,14,3,8,13,2,7,12,1,6,11
#hàm dịch vòng trái đối với plaintext
def shift_rows(state=""):
    res=""
    #mảng trên
    for i in [0,5,10,15,
              4,9,14,3,
              8,13,2,7,
              12,1,6,11]:
        res=res+state[i*2:i*2+2]
    return res
#hàm nhân 2 hexa rồi mod cho ma trận mod trả về dec
def hex_mul(hex1,hex2):
    if not all(char in "0123456789ABCDEFabcdef" for char in hex1+hex2):
        raise ValueError("hexa invalid")
    #bin->dec
    mod=int("100011011",2)
    #hex->dec
    hex1=int(hex1,16)
    hex2=int(hex2,16)
    res=0
    for i in range(hex1.bit_length()):
        if hex1>>i&1 :
            res ^= hex2<<i
    while res.bit_length()>=9:
        res^=mod<<(res.bit_length()-9)
    return res
#hàm mix_columns
def mix_columns(state):
    default_matrix = [
        "02", "03", "01", "01",
        "01", "02", "03", "01",
        "01", "01", "02", "03",
        "03", "01", "01", "02"
    ]
    #xoay chiều hàng thành cột cột thành hàng của state
    state_matrix= [state[i*2:i*2+2] for i in [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]]
    result=""
    for i in [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]:
        # hàng của ma trận cố định, cột của ma trận trạng thái
        row=int(i/4)
        col=i%4
        temp=0
        temp^=hex_mul(default_matrix[row*4+0],state_matrix[4*0+col])
        temp^=hex_mul(default_matrix[row*4+1],state_matrix[4*1+col])
        temp^=hex_mul(default_matrix[row*4+2],state_matrix[4*2+col])
        temp^=hex_mul(default_matrix[row*4+3],state_matrix[4*3+col])
        result+=hex(temp)[2:].zfill(2)
        
    return result.upper()

#Tính kết quả AddRoundKey
state= AddRoundKey(m,k[0])
#Thay thế từng byte trong state bằng bảng S-box SubByte
state=replaceS_box(state)
#Dịch vòng trái các byte trong state ShiftRows
state = shift_rows(state)
#Trộn các byte trong state MixColumns
state = mix_columns (state)
# print(state)
#Dịch vòng trái các byte trong state AddRoundKey
state = AddRoundKey(state, k[1])
#===================== 8 VÒNG LẶP ===========
for i in range(2,10):
    print(state,k[i])
    state=replaceS_box(state)
    state = shift_rows(state)
    state = mix_columns (state)
    state = AddRoundKey(state, k[i])
#Vòng lặp cuối (lần lặp 10) 
C = state = AddRoundKey(shift_rows( replaceS_box(state)), k[10])
print(C)