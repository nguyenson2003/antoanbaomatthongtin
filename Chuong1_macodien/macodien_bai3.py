def vigenere_autokey_encrypt(text, key):# m,k
    return "".join([chr((ord(i)+ord(j)-ord('A')-ord('A'))%26+ord('A')) for i,j in zip(text,key+text)])

def vigenere_autokey_decrypt(text, key):# m,k
    res = []
    for i in range(len(text)):
        res.append( chr((ord(text[i])-ord(key[i] if i<len(key) else res[i-len(key)])-ord('A')-ord('A')+26*26)%26+ord('A')))
    return "".join(res)

# print(vigenere_autokey_encrypt("THETRUTHWILLO","THEGRASS"))
# print(vigenere_autokey_decrypt("EZWPPRFPUJQFNUX","BLACK"))
f = open("Chuong1_macodien/input3.txt", "r")
plaintext = f.readline()
key = f.readline()
print(vigenere_autokey_encrypt(plaintext,key))