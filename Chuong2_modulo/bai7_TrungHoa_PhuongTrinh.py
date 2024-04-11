def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            m1, m2, m3, a1, a2, a3 = map(int, file.read().split())
            return m1, m2, m3, a1, a2, a3
    except FileNotFoundError:
        print(f"File '{filename}' khong ton tai.")
        return None, None, None, None, None, None
    except Exception as e:
        print(f"loi file  '{filename}': {e}")
        return None, None, None, None, None, None

def dinh_ly_TrungHoa(m1, m2, m3, a1, a2, a3):
    M = m1 * m2 * m3
    
    M1 = M // m1
    M2 = M // m2
    M3 = M // m3
    
    M1_inverse = pow(M1, -1, m1)
    M2_inverse = pow(M2, -1, m2)
    M3_inverse = pow(M3, -1, m3)
    
    x = (a1 * M1 * M1_inverse + a2 * M2 * M2_inverse + a3 * M3 * M3_inverse) % M
    
    return x

# Đọc giá trị m1, m2, m3, a1, a2, a3 từ file input
input_filename = "Chuong2_modulo/input.txt"
m1, m2, m3, a1, a2, a3 = read_input_file(input_filename)

if m1 is not None and m2 is not None and m3 is not None and a1 is not None and a2 is not None and a3 is not None:
    result = dinh_ly_TrungHoa(m1, m2, m3, a1, a2, a3)
    print("ket qua sau khi giai he pt x= :", result)
else:
    print("loi khi doc file.")
