# Các giá trị đã cho
q = 7207
a = 3
xA = 422
xB = 286

# Tính khóa công khai và khóa phiên cho An
yA = pow(a, xA, q)
K_A = pow(yB, xA, q)

# Tính khóa công khai và khóa phiên cho Ba
yB = pow(a, xB, q)
K_B = pow(yA, xB, q)

# In ra kết quả
print("a: Khóa công khai của An: yA =", yA, " Khóa phiên K =", K_A)
print("b: Khóa công khai của Ba: yB =", yB, " Khóa phiên K =", K_B)
