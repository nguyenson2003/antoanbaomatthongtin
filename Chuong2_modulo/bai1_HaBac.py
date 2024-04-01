def power_mod(a, m, n):
    result = 1
    a = a % n
    while m > 0:
        if m % 2 == 1:
            result = (result * a) % n
        m = m >> 1
        a = (a * a) % n
    return result

# tinh modulo
a = 239
m = 6653
n = 6653

print(f"{a} mũ {m} modulo {n} = {power_mod(a, m, n)}")