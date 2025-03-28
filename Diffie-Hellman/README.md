# Diffie-Hellman Key Exchange  

This program implements the **Diffie-Hellman Key Exchange** algorithm, allowing two parties to securely generate a shared secret key over an insecure channel.  

## Features  
- Uses a prime number and a primitive root as public parameters.  
- Generates private keys for both users.  
- Computes public keys and exchanges them.  
- Derives a shared secret key independently on both sides.  
- Verifies that both parties compute the same shared key.  

## How It Works  
1. A prime number (**p**) and a primitive root (**g**) are chosen as public parameters.  
2. Two users (A and B) generate their private keys randomly.  
3. Each user computes their public key using **(g^private_key) mod p**.  
4. Public keys are exchanged.  
5. Both users compute a shared secret key using the received public key and their own private key.  
6. The computed shared keys are verified to be identical.  

## How to Run  
### Google Colab link: 
https://colab.research.google.com/drive/1vKEWiGpvVcnu_bvJtYfVs-qzNOAagSSm?authuser=2#scrollTo=IrvF1B9ErsSQ
### Run Locally  
1. Install Python 3.x if not installed.  
2. Copy the script into a Python file (`diffie_hellman.py`).  
3. Run the script:  
   ```bash
   python diffie_hellman.py
