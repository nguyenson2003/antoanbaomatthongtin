import math

def is_primitive_root(a, n):
    sqrt_n = int(math.sqrt(n))
    if a <= 1 or n <= 1:
        return False
    if a == 2 or a == 3:
        return True
    if n % a == 0:
        return False
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

A = int(input("Nhập giá trị của số nguyên A: "))
N = int(input("Nhập giá trị của số nguyên N: "))

if is_primitive_root(A, N):
    print(f"{A} là một căn nguyên thủy của {N}.")
else:
    print(f"{A} không phải là một căn nguyên thủy của {N}.")
