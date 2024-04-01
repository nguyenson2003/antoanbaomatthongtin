def extended_euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return (gcd, y, x - (a // b) * y)

def mod_inverse(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        raise Exception('Không có nghịch đảo modulo với số này.')
    else:
        return x % m

# Nhập giá trị a và n từ người dùng
a = int(input("Nhập giá trị a: "))
n = int(input("Nhập giá trị n: "))

# Tìm nghịch đảo và in ra kết quả
try:
    inv = mod_inverse(a, n)
    print("Nghịch đảo của", a, "modulo", n, "là:", inv)
except Exception as e:
    print(e)
