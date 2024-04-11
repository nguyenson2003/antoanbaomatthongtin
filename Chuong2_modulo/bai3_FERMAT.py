def power_modulo(a, m, n):
    if m == 0:
        return 1 % n
    result = power_modulo(a, m // 2, n)
    result = (result * result) % n
    if m % 2 == 1:
        result = (result * a) % n
    return result

if __name__ == "__main__":
    # Đọc từ file input
    with open("Chuong2_modulo/input.txt", "r") as file:
        a, m, n = map(int, file.readline().split())
    
    # Tính lũy thừa modulo
    result = power_modulo(a, m, n)
    
    # In kết quả
    print("a^m mod n =", result)
