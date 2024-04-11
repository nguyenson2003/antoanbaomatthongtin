def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            key, plaintext = file.read().splitlines()
            return int(key), plaintext
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None, None

def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(key):
        for j in range(i, len(plaintext), key):
            ciphertext += plaintext[j]
    return ciphertext

# Đọc khóa và văn bản cần mã hóa từ file input
input_filename = "input.txt"
key, plaintext = read_input_file(input_filename)

if key is not None and plaintext is not None:
    # Mã hóa văn bản
    ciphertext = encrypt(plaintext, key)
    print("Cipher Text:", ciphertext)
else:
    print("Cannot proceed due to error in reading input file.")
