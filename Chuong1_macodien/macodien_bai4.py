def encrypt(text, key):
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
# plaintext = "abcdefghijklmnopqrstuvwxyz"
# key = "JEHFAVZNOXUBMYPKDLGSRCTWQI"

# encrypted_text = encrypt(plaintext, key)
# print("Decrypted text:", encrypted_text)
# #câu 4
# print("Decrypted text 2:", encrypt("MONEYMAKESTHEMAR", "JEHFAVZNOXUBMYPKDLGSRCTWQI"))
f = open("Chuong1_macodien/input4.txt", "r")
plaintext = f.readline()
key = f.readline()
print(encrypt(plaintext,key))