def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
                cipher_text += chr(shift)
            else:
                if shift > ord('Z'):
                    shift -= 26
                cipher_text += chr(shift)
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                if shift < ord('a'):
                    shift += 26
                plain_text += chr(shift)
            else:
                if shift < ord('A'):
                    shift += 26
                plain_text += chr(shift)
        else:
            plain_text += char
    return plain_text

text = input("Enter your text here: ")
key = int(input("input the key, or shift value: "))

if __name__ == "__main__":
    plain_text = "HELLO WORLD"
    cipher_text = encrypt(text, key)
    print("Encrypted text:", cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print("Decrypted text:", decrypted_text)
