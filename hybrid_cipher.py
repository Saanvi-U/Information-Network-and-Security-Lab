from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

# AES Substitution Cipher (128-bit)
def aes_substitution(text, key, decrypt=False):
    key = key.ljust(16)[:16].encode('utf-8')  # Ensure 16-byte key
    cipher = AES.new(key, AES.MODE_ECB)  # ECB mode (for simplicity, NOT for real security)
    
    if decrypt:
        return unpad(cipher.decrypt(bytes.fromhex(text)), AES.block_size).decode('utf-8')
    else:
        return cipher.encrypt(pad(text.encode('utf-8'), AES.block_size)).hex()

# Transposition Cipher (Shuffle the text with a fixed seed)
def transposition(text, seed, decrypt=False):
    random.seed(seed)  # Use a fixed seed for reproducibility
    indices = list(range(len(text)))
    random.shuffle(indices)
    
    if decrypt:
        key_inv = sorted(range(len(indices)), key=indices.__getitem__)  # Inverse mapping
        return ''.join([text[i] for i in key_inv])
    else:
        return ''.join([text[i] for i in indices])

# Hybrid Cipher combining AES Substitution and Transposition
def hybrid_cipher(text, key, decrypt=False):
    seed = sum(ord(c) for c in key)  # Generate a simple numerical seed from the key
    
    if decrypt:
        text = transposition(text, seed, decrypt=True)
        return aes_substitution(text, key, decrypt=True)
    else:
        text = aes_substitution(text, key, decrypt=False)
        return transposition(text, seed, decrypt=False)

# Example usage
plaintext = "HELLO WORLD"
aes_key = "thisis128bitkey"

# Encrypt the plaintext
encrypted = hybrid_cipher(plaintext, aes_key)
print("Encrypted:", encrypted)

# Decrypt the ciphertext
decrypted = hybrid_cipher(encrypted, aes_key, decrypt=True)
print("Decrypted:", decrypted)
