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

# Khóa riêng và khóa công khai của An
q = 7349
a = 3
x_A = 366
Y_A = power_mod(a, x_A, q)

# Bản mã của Ba
M = 333
k = 32
C1 = power_mod(a, k, q)
s = power_mod(C1, x_A, q)
s_inv = mod_inverse(s, q)
C2 = (s_inv * M) % q

# Giải mã bản mã
decrypted_M = (C2 * mod_inverse(power_mod(C1, x_A, q), q)) % q

print("Khóa công khai của An (PU):", q, a, Y_A)
print("Bản mã của Ba (C1, C2):", C1, C2)
print("Bản tin gốc sau khi giải mã:", decrypted_M)
