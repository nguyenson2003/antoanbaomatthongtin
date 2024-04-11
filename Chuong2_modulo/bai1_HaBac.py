def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            a, m, n = map(int, file.read().split())
            return a, m, n
    except FileNotFoundError:
        print(f"File '{filename}' khong ton tai.")
        return None, None, None
    except Exception as e:
        print(f"loi doc file '{filename}': {e}")
        return None, None, None

def mod_exp(a, m, n):
    if m == 0:
        return 1
    elif m % 2 == 0:
        half_power = mod_exp(a, m // 2, n)
        return (half_power * half_power) % n
    else:
        return (a * mod_exp(a, m - 1, n)) % n

# Đọc giá trị a, m, n từ file input
input_filename = "Chuong2_modulo/input.txt"
a, m, n = read_input_file(input_filename)

if a is not None and m is not None and n is not None:
    result = mod_exp(a, m, n)
    print(f"kq {a}^{m} mod {n} la:", result)
else:
    print("loi khi doc file.")
