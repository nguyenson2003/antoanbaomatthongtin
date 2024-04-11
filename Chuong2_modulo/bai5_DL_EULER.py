def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

def power_modulo(a, m, n):
    result = 1
    for _ in range(m):
        result = (result * a) % n
    return result

if __name__ == "__main__":
    # Đọc từ file input
    with open("Chuong2_modulo/input.txt", "r") as file:
        a, m, n = map(int, file.readline().split())
    
    # Tính phi(n) dùng Định lý Euler
    phi_n = phi(n)
    
    # Tính lũy thừa modulo
    result = power_modulo(a, m % phi_n, n)
    
    # In kết quả
    print("a^m mod n =", result)
