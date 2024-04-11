def generate_playfair_matrix(key):
    # Tạo ma trận 5x5 từ khóa
    key = key.replace("J", "I")  # Loại bỏ 'J' và thay thế bằng 'I'
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_set:
            key += char
            key_set.add(char)
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, char):
    # Tìm vị trí của ký tự trong ma trận
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace("J", "I")  # Chuyển đổi văn bản thành chữ hoa và thay thế 'J' bằng 'I'
    plaintext = plaintext.replace(" ", "")  # Loại bỏ khoảng trắng
    # Chia văn bản thành các cặp ký tự
    pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i+1]:
            pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            pairs.append(plaintext[i:i+2])
            i += 2
    # Mã hóa từng cặp ký tự
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(key_matrix, pair[0])
        row2, col2 = find_position(key_matrix, pair[1])
        if row1 == row2:  # Nếu nằm trên cùng một hàng
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Nếu nằm trên cùng một cột
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:  # Nếu không cùng hàng cũng không cùng cột
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext

def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

# Đọc văn bản và khóa từ file input
input_filename = "inputB4C1.txt"
input_data = read_input_file(input_filename)

if input_data:
    key, text_Plain = input_data  # Unpack giá trị trả về từ hàm read_input_file
    # Thực hiện mã hóa và các bước tiếp theo...
else:
    print("Không thể tiếp tục do lỗi khi đọc tệp input.txt.")

# Tạo ma trận từ khóa
key_matrix = generate_playfair_matrix(key)

# Mã hóa văn bản
encrypted_text = encrypt(text_Plain, key_matrix)

print("Văn bản mã hóa:", encrypted_text)
