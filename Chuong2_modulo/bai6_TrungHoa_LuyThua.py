def power_mod(a, k, n):
    result = 1
    a = a % n  # Giảm thiểu số lượng phép nhân
    while k > 0:
        # Nếu k lẻ, nhân kết quả với a và lấy số dư trung hoa với n
        if k % 2 == 1:
            result = (result * a) % n
        # Chia k cho 2 và lấy số dư trung hoa của a với n
        k = k // 2
        a = (a * a) % n
    return result

# Nhập giá trị a, k và n từ người dùng
a = int(input("Nhập giá trị a: "))
k = int(input("Nhập giá trị k: "))
n = int(input("Nhập giá trị n: "))

# Tính lũy thừa modulo và in ra kết quả
result = power_mod(a, k, n)
print("Kết quả:", result)
