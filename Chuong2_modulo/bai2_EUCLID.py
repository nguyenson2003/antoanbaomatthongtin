def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            a, m = map(int, file.read().split())
            return a, m
    except FileNotFoundError:
        print(f"file'{filename}' ko ton tai.")
        return None, None
    except Exception as e:
        print(f"loi doc file '{filename}': {e}")
        return None, None

def euclid_mo(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = euclid_mo(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def tinh_modulo(a, m):
    gcd, x, y = euclid_mo(a, m)
    if gcd != 1:
        return None  # Nếu không tồn tại nghịch đảo
    else:
        return x % m

# Đọc giá trị a, m từ file input
input_filename = "Chuong2_modulo/input.txt"
a, m = read_input_file(input_filename)

if a is not None and m is not None:
    inverse = tinh_modulo(a, m)
    if inverse is not None:
        print(f"nghich dao modulo {a} mod {m} la:", inverse)
    else:
        print(f"khong tinh duoc nghich dao modulo {a} mod {m}.")
else:
    print("loi khi doc file.")
