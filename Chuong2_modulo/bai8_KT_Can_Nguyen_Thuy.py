def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def can_nguyen_thuy(a, n):
    if gcd(a, n) != 1:
        return False
    phi_n = n - 1  # Hàm phi Euler cho số nguyên n
    factors = set()
    m = phi_n
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            factors.add(i)
            while m % i == 0:
                m //= i
    if m > 1:
        factors.add(m)
    for p in factors:
        if pow(a, phi_n // p, n) == 1:
            return False
    return True

if __name__ == "__main__":
    # Đọc từ file input
    with open("Chuong2_modulo/input.txt", "r") as file:
        a, n = map(int, file.readline().split())
    
    # Kiểm tra xem a có phải là căn nguyên thủy của n không
    if can_nguyen_thuy(a, n):
        print(f"{a} là một căn nguyên thủy của {n}")
    else:
        print(f"{a} không là một căn nguyên thủy của {n}")
