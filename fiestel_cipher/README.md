# Feistel Cipher Implementation

This folder contains a Python implementation of the Feistel cipher. It demonstrates encryption and decryption using a Feistel network with an XOR-based round function.

## Features
- Implements the Feistel cipher for encryption and decryption.
- Uses a simple XOR-based round function.
- Supports key-based encryption.
- Demonstrates how Feistel networks work.

## Usage

### Encryption
```python
key = "key123"
text = "hello123"
encrypted_text = feistel_encrypt(text, key)
print("Encrypted:", encrypted_text)
```

### Decryption
```python
decrypted_text = feistel_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text.strip())
```

## How to Run
To run this code in a Jupyter Notebook environment, click the link below:

https://colab.research.google.com/drive/1nTMKuSWba2JFK-cUegJcIKdfEVK-ZsEn?usp=sharing
## Example
```plaintext
Enter the key: key123
Enter the message: hello123
Encrypted: <ciphertext>
Decrypted: hello123
```

## Code Explanation
### Key Processing
- The key is used to generate round subkeys for encryption and decryption.

### Message Preparation
- The message is split into two halves for the Feistel process.
- If the message has an odd length, padding is applied.

### Encryption Process
- The Feistel cipher performs multiple rounds of processing.
- In each round:
  - The right half is processed with the round function (XOR with the key).
  - The left half is XORed with the result of the round function.
  - The halves are swapped.
- After the final round, the halves are concatenated to produce the ciphertext.

### Decryption Process
- The process is reversed by applying the same operations in reverse order.
- The original plaintext is reconstructed after all rounds are reversed.

## Requirements
- Python 3.x

## Contributing
Feel free to submit issues or pull requests to improve the implementation!

