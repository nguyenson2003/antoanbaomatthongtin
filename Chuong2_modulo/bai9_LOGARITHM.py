def discrete_logarithm(a, b, n):
    m = int(n ** 0.5) + 1

    # Tính danh sách baby steps
    baby_steps = {}
    for j in range(m):
        baby_steps[pow(a, j, n)] = j

    # Tính giant steps và kiểm tra xem có phải là logarithm rời rạc hay không
    giant_step = pow(a, m * (n - 2), n)
    for i in range(m):
        if b in baby_steps:
            return i * m + baby_steps[b]
        else:
            b = (b * giant_step) % n

    return None

# Sử dụng ví dụ
a = 2
b = 7
n = 11
result = discrete_logarithm(a, b, n)
if result is not None:
    print(f"logarithm cua {b} voi co so {a} modulo {n} la {result}.")
else:
    print(f"khong tim duoc logarithm cua {b} voi co so {a} modulo {n}.")
