# RSA Encryption and Decryption  

This program implements a basic RSA encryption and decryption system using two prime numbers. It calculates public and private keys, encrypts a message, and then decrypts it back to its original form.  

## Features  
- Generates RSA public and private keys.  
- Encrypts a given numerical message.  
- Decrypts the message back to its original value.  

## How It Works  
1. The user inputs two prime numbers (**p** and **q**).  
2. The program calculates:  
   - **n** = p × q  
   - **ϕ(n)** = (p - 1) × (q - 1)  
3. A public key exponent (**e**) is chosen such that **gcd(e, ϕ(n)) = 1**.  
4. The private key exponent (**d**) is computed using the modular inverse.  
5. The message is encrypted using **C = M^e mod n**.  
6. The ciphertext is decrypted using **M = C^d mod n**.  

## How to Run  
### Colab link: 
https://colab.research.google.com/drive/1qE3xpwKy8YNoS6-XqgvhpVabEPrcAcCw?authuser=2#scrollTo=RvaPlilYrOAd
### Run Locally  
1. Install Python 3.x if not installed.  
2. Copy the script into a Python file (`rsa.py`).  
3. Run the script:  
   ```bash
   python rsa.py
