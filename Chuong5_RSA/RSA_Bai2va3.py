# Hàm tính ước số chung lớn nhất (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tìm số nghịch đảo theo mod
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Các giá trị đã cho
p = 31
q = 47
e = 43
M = 53

# Tính n
n = p * q

# Tính hàm số Euler: φ(n)
phi_n = (p - 1) * (q - 1)

# Tìm số nguyên d thỏa mãn gcd(d, φ(n)) = 1 và d < φ(n)
d = mod_inverse(e, phi_n)

# Bản mã hóa
C = pow(M, e, n)

# Bản giải mã
decrypted_M = pow(C, d, n)

# In ra kết quả
print("a: Khóa công khai của An: PU = {" + str(e) + ", " + str(n) + "}")
print("b: Khóa riêng của An: PR = {" + str(d) + ", " + str(n) + "}")
print("c: Bản mã hóa của M =", C)
print("d: Bản giải mã của C =", decrypted_M)
