def power_mod_Fermat(a, m, n):
    # Kiểm tra nếu n là số nguyên tố
    if not is_prime(n):
        raise ValueError("n phải là số nguyên tố để sử dụng định lý Fermat.")
    
    # Áp dụng Định lý Fermat
    return pow(a, m % (n - 1), n)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Nhập giá trị a, m, và n từ người dùng
a = int(input("Nhập giá trị a: "))
m = int(input("Nhập giá trị mũ m: "))
n = int(input("Nhập giá trị n: "))

# Tính lũy thừa modulo và in ra kết quả
try:
    result = power_mod_Fermat(a, m, n)
    print("Kết quả:", result)
except ValueError as e:
    print(e)
