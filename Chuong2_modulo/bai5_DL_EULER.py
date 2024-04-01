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

def power_mod_Euler(a, m, n):
    # Tính giá trị của hàm Euler phi(n)
    phi_n = euler_phi(n)
    
    # Sử dụng Định lý Euler để tính lũy thừa modulo
    return pow(a, m % phi_n, n)

# Nhập giá trị a, m và n từ người dùng
a = int(input("Nhập giá trị a: "))
m = int(input("Nhập giá trị mũ m: "))
n = int(input("Nhập giá trị n: "))

# Tính lũy thừa modulo và in ra kết quả
result = power_mod_Euler(a, m, n)
print("Kết quả:", result)
