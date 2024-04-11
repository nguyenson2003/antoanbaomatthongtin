# Hàm tính lũy thừa modulo
def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

# Hàm tìm nghịch đảo modulo
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Thông số
p = 59
q = 29
h = 10
x_A = 2
k = 3
M_hash = 10  # Giả sử băm bản tin M cho được giá trị này

# Tính g và y_A
g = power_mod(h, (p-1)//q, p)
y_A = power_mod(g, x_A, p) % q

# Tạo chữ ký số của An
r = power_mod(g, k, p) % q
s = (mod_inverse(k, q) * (M_hash + x_A * r)) % q

# Ba xác minh chữ ký số
w = mod_inverse(s, q)
u1 = (M_hash * w) % q
u2 = (r * w) % q
v = ((power_mod(g, u1, p) * power_mod(y_A, u2, p)) % p) % q

signature_valid = (v == r)

print("Khóa công khai của An (y_A):", y_A)
print("Chữ ký số của An (r, s):", r, s)
print("Chữ ký số có hợp lệ:", signature_valid)
