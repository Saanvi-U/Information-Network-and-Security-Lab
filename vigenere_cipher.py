def vigenere(text, key, decrypt=False):
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    shift = -1 if decrypt else 1
    return ''.join(chr((ord(c) - 65 + shift * (ord(k) - 65)) % 26 + 65) if c.isalpha() else c for c, k in zip(text.upper(), key.upper()))

# Example Usage
plaintext = "HELLO"
key = "KEY"
ciphertext = vigenere(plaintext, key)
decrypted = vigenere(ciphertext, key, decrypt=True)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
