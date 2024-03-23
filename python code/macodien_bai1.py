def caesar_encrypt(text, shift):# m,k
    text=text.upper()
    encrypted_text = ""
    for char in text:
        if char.isalpha():#kiểm tra xem text phải là chữ không
            #ord('a') lấy ra mã ascii của chữ a
            #
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text
print(caesar_encrypt("abcdefghijklmnopqrstuvwxyz",1))
#câu 1

print(caesar_encrypt("STILLWATERSRUNDE",17))