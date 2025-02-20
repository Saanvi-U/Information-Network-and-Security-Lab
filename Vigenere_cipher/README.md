# Vigenère Cipher Implementation

This folder contains a Python implementation of the Vigenère cipher. It demonstrates encryption and decryption using a key-based polyalphabetic substitution method.

## Features
- Implements the Vigenère cipher for encryption and decryption.
- Uses a repeating key pattern to shift characters.
- Supports both encryption and decryption modes.
- Maintains non-alphabetic characters unchanged.

## Usage

### Encryption
```python
plaintext = "HELLO"
key = "KEY"
ciphertext = vigenere(plaintext, key)
print("Ciphertext:", ciphertext)
```

### Decryption
```python
decrypted_text = vigenere(ciphertext, key, decrypt=True)
print("Decrypted:", decrypted_text)
```

## How to Run
To run this code in a Jupyter Notebook environment, click the link below:

https://colab.research.google.com/drive/1czgJhiGb9Hs9b9yv8QtQKi3--fPTLgnq?usp=sharing

## Example
```plaintext
Enter the key: KEY
Enter the message: HELLO
Encrypted: RIJVS
Decrypted: HELLO
```

## Code Explanation
### Key Processing
- The key is repeated to match the length of the message.
- Both the key and message are converted to uppercase for consistency.

### Encryption Process
- Each letter of the plaintext is shifted by the corresponding letter in the key.
- The formula used is:
  - `Encrypted character = (Plaintext character + Key character) mod 26`
- Non-alphabetic characters remain unchanged.

### Decryption Process
- The reverse shift is applied to retrieve the original text.
- The formula used is:
  - `Decrypted character = (Ciphertext character - Key character) mod 26`

## Requirements
- Python 3.x

## Contributing
Feel free to submit issues or pull requests to improve the implementation!

