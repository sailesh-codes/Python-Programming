# Simple Caesar Cipher

def encrypt(text, shift):
    result = ""
    for ch in text:
        result += chr((ord(ch) + shift))
    return result

def decrypt(text, shift):
    result = ""
    for ch in text:
        result += chr((ord(ch) - shift))
    return result


msg = input("Enter a message: ")
shift = 3  # fixed shift value

enc = encrypt(msg, shift)
print("Encrypted:", enc)

dec = decrypt(enc, shift)
print("Decrypted:", dec)
