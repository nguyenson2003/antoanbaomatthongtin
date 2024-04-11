def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            a, k, n = map(int, file.read().split())
            return a, k, n
    except FileNotFoundError:
        print(f"File '{filename}' khong ton tai.")
        return None, None, None
    except Exception as e:
        print(f"loi file '{filename}': {e}")
        return None, None, None

def dinh_ly_TrungHoa(a, k, n):
    b = 1
    for i in range(k):
        b = (b * a) % n
    return b

# Đọc giá trị a, k, n từ file input
input_filename = "Chuong2_modulo/input.txt"
a, k, n = read_input_file(input_filename)

if a is not None and k is not None and n is not None:
    result = dinh_ly_TrungHoa(a, k, n)
    print(f"ket qua {a}^{k} mod {n} la:", result)
else:
    print("loi khong the doc file.")
