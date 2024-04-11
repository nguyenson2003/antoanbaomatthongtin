def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def diffie_hellman(q, a, xA, xB):
    # Tính yA và yB
    yA = power_mod(a, xA, q)
    yB = power_mod(a, xB, q)

    # Tính khóa phiên K
    K_A = power_mod(yB, xA, q)
    K_B = power_mod(yA, xB, q)

    return yA, yB, K_A, K_B

# Số nguyên tố và số nguyên thủy
q = 7207
a = 3

# Khóa riêng của An và Ba
xA = 422
xB = 286

# Giải bài toán
yA, yB, K_A, K_B = diffie_hellman(q, a, xA, xB)

print("yA =", yA)
print("yB =", yB)
print("Khóa phiên của An (K_A) =", K_A)
print("Khóa phiên của Ba (K_B) =", K_B)
