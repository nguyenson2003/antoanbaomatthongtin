def euler_phi(n):
    result = n  # Khởi tạo kết quả bằng n
    
    # Phân tích n thành các thừa số nguyên tố và loại bỏ các thừa số trùng lặp
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result *= (1.0 - (1.0 / p))
        p += 1
    
    # Xử lý trường hợp n còn lại là một số nguyên tố
    if n > 1:
        result *= (1.0 - (1.0 / n))
    
    return int(result)

# Nhập giá trị n từ người dùng
n = int(input("Nhập giá trị n: "))

# Tính giá trị của hàm Euler và in ra kết quả
phi_n = euler_phi(n)
print("Giá trị của hàm Euler phi(", n, ") =", phi_n)
