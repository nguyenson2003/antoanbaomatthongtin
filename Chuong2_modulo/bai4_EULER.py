def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            n = int(file.read())
            return n
    except FileNotFoundError:
        print(f" File '{filename}' ko ton tai.")
        return None
    except Exception as e:
        print(f"loi doc file '{filename}': {e}")
        return None

def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Đọc giá trị n từ file input
input_filename = "Chuong2_modulo/input.txt"
n = read_input_file(input_filename)

if n is not None:
    euler_value = euler_phi(n)
    print(f"ket qua phi({n}) la:", euler_value)
else:
    print("loi khi doc file.")
