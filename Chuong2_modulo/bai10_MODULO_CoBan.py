def basic_modulo_operations(a, b, x, y, n):
    # Biểu thức 1: A1 = (a*x + b*y) mod n
    A1 = ((a * x) % n + (b * y) % n) % n

    # Biểu thức 2: A2 = (a*x - b*y) mod n
    A2 = ((a * x) % n - (b * y) % n) % n

    # Biểu thức 3: A3 = (a*x * b*y) mod n
    A3 = ((a * x) % n * (b * y) % n) % n

    # Biểu thức 4: A4 = (b*y)^-1 mod n
    A4 = pow((b * y) % n, -1, n)  # Sử dụng pow với số mũ âm để tính nghịch đảo modulo

    # Biểu thức 5: A5 = (a*x / b*y) mod n
    A5 = ((a * x) % n * pow((b * y) % n, -1, n)) % n

    return A1, A2, A3, A4, A5

# Nhập các giá trị từ người dùng
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
x = int(input("Nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))
n = int(input("Nhập giá trị n: "))

# Tính các biểu thức modulo cơ bản
result = basic_modulo_operations(a, b, x, y, n)

# In ra kết quả
print("Biểu thức 1 (A1):", result[0])
print("Biểu thức 2 (A2):", result[1])
print("Biểu thức 3 (A3):", result[2])
print("Biểu thức 4 (A4):", result[3])
print("Biểu thức 5 (A5):", result[4])
