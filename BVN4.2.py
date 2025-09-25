def encrypt_caesar(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + k) % 26 + base)
            ciphertext += new_char
        else:
            ciphertext += char  
    return ciphertext

P = "NguyenThiTramAnh"
k = 3

C = encrypt_caesar(P, k)
print("Plaintext:", P)
print("Ciphertext:", C)
