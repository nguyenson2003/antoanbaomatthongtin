def vigenere_onekey_encrypt(text, key):# m,k
    return "".join([chr((ord(i)+ord(j)-ord('A')-ord('A'))%26+ord('A')) for i,j in zip(text,key*(len(text) // len(key) + 1))])

def vigenere_onekey_decrypt(text, key):# m,k
    return "".join([chr((ord(i)-ord(j)-ord('A')-ord('A')+26)%26+ord('A')) for i,j in zip(text,key*(len(text) // len(key) + 1))])

# print(vigenere_onekey_encrypt("ATFIVEHEADNORTHTOTRENCHES","FINAL"))
# print(vigenere_onekey_decrypt("AMZBVEFYOSMF","ABOVE"))
f = open("Chuong1_macodien/input2.txt", "r")
plaintext = f.readline()
key = f.readline()
print(vigenere_onekey_encrypt(plaintext,key))