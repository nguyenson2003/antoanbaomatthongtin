def caesar_encrypt(text, key):# m,k
    return "".join([chr((ord(i)+ord(j)-ord('A')-ord('A'))%26+ord('A')) for i,j in zip(text,key*(len(text) // len(key) + 1))])
#câu 1

print(caesar_encrypt("THETRUTHWILLO","THEGRASS"))