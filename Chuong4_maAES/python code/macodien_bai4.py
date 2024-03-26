def decrypt(text, key):
    decrypted_text = ""
    #auto viết thường
    text=text.upper()
    for char in text:
        if char.isalpha():
            #lấy ra vị trí của decrypt_char in key
            index = ord(char) - ord('A')
            decrypted_char = key[index].upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
encrypted_text = "abcdefghijklmnopqrstuvwxyz"
key = "JEHFAVZNOXUBMYPKDLGSRCTWQI"

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
#câu 4
print("Decrypted text 2:", decrypt("MONEYMAKESTHEMAR", "JEHFAVZNOXUBMYPKDLGSRCTWQI"))