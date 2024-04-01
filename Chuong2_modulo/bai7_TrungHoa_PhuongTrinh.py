def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_modular_equation(a1, b1, a2, b2, a3, b3, n):
    # Tìm gcd giữa a1 và a2
    gcd1, x0, _ = gcd_extended(a1, a2)
    
    # Kiểm tra nếu gcd1 không chia hết cho a3
    if a3 % gcd1 != 0:
        return "Không có nghiệm"
    
    # Tìm nghiệm modulo
    x0 %= n // gcd1
    x = (x0 * (b2 - b1) // gcd1) % (n // gcd1)
    
    # Kiểm tra từng giá trị x có thỏa mãn phương trình thứ hai hay không
    solutions = []
    for k in range(gcd1):
        xk = x0 + k * (n // gcd1)
        xk %= n
        if (a2 * xk) % n == b2:
            # Kiểm tra nếu xk thỏa mãn cả hai phương trình
            if (a3 * xk) % n == b3:
                solutions.append((xk, k))
    
    if not solutions:
        return "Không có nghiệm"
    
    return solutions

# Nhập các hệ số và modulo từ người dùng
a1 = int(input("Nhập hệ số a1: "))
b1 = int(input("Nhập hệ số b1: "))
a2 = int(input("Nhập hệ số a2: "))
b2 = int(input("Nhập hệ số b2: "))
a3 = int(input("Nhập hệ số a3: "))
b3 = int(input("Nhập hệ số b3: "))
n = int(input("Nhập modulo n: "))

# Giải hệ phương trình modulo và in ra kết quả
result = solve_modular_equation(a1, b1, a2, b2, a3, b3, n)
print("Nghiệm của hệ phương trình modulo:", result)
