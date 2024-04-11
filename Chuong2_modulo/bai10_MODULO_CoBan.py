def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            a, b, x, y, n = map(int, file.read().split())
            return a, b, x, y, n
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None, None, None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None, None, None, None, None

def compute_expressions(a, b, x, y, n):
    A1 = (a * x + b * y) % n
    A2 = (a * x - b * y) % n
    A3 = (a * x * b * y) % n
    A4 = pow(b * y, -1, n)
    A5 = (a * x * pow(b * y, -1, n)) % n
    return A1, A2, A3, A4, A5

# Đọc giá trị a, b, x, y, n từ file input
input_filename = "Chuong2_modulo/input.txt" 
a, b, x, y, n = read_input_file(input_filename)

if (a is not None and b is not None and x is not None and y is not None and n is not None):
    # Tính các biểu thức modulo cơ bản
    A1, A2, A3, A4, A5 = compute_expressions(a, b, x, y, n)
    # In kết quả
    print("A1 =", A1)
    print("A2 =", A2)
    print("A3 =", A3)
    print("A4 =", A4)
    print("A5 =", A5)
else:
    print("loi khi doc file.")
