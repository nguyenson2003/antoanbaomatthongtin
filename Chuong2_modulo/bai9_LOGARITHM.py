def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            a, b, n = map(int, file.read().split())
            return a, b, n
    except FileNotFoundError:
        print(f"File '{filename}' khong ton tai.")
        return None, None, None
    except Exception as e:
        print(f"loi file '{filename}': {e}")
        return None, None, None

def logarit_RoiRac(a, b, n):
    k = 0
    while pow(a, k, n) != b:
        if k > n-1:
            return -1
        k += 1
    return k

# Đọc giá trị a, b, n từ file input
input_filename = "Chuong2_modulo/input.txt" 
a, b, n = read_input_file(input_filename)

if a is not None and b is not None and n is not None:
    # Tìm logarithm rời rạc của b với cơ số a modulo n
    result = logarit_RoiRac(a, b, n)
    if result == -1:
        print("Không tìm thấy logarithm rời rạc của", b, "với cơ số", a, "modulo", n)
    else:
        print("Logarithm rời rạc của", b, "với cơ số", a, "modulo", n, "là:", result)
else:
    print("loi doc file.")
