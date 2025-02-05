# Hill Cipher Encryption in Python

This repository contains a Python implementation of the Hill cipher encryption. It uses a key matrix to encrypt plaintext in blocks.

## Description

The Hill cipher is a polygraphic substitution cipher based on linear algebra. It encrypts plaintext in blocks of *n* letters, where *n* is the dimension of the square key matrix.  Each block of plaintext is transformed into a block of ciphertext using matrix multiplication and modulo arithmetic.

This implementation handles:

*   Uppercase letters.
*   Padding: If the plaintext length is not a multiple of the key matrix dimension, 'X' characters are appended for padding.
*   Matrix multiplication and modulo 26 arithmetic for encryption.

## How to Use

1.  You can run this code directly in Google Colab using the link provided below.

   https://colab.research.google.com/drive/1pU8OFx7Jx-MDVosIlKuBaN9cM6-0jGYZ?usp=sharing
   

## Code Explanation

The `hill_cipher_encrypt(plaintext, key_matrix)` function:

1.  **Preprocessing:**
    *   Converts the `plaintext` to uppercase and removes spaces.
    *   Pads the `plaintext` with 'X' characters if its length is not a multiple of `n` (the dimension of the key matrix).

2.  **Encryption:**
    *   Converts the `plaintext` into a vector of numerical values (0-25 representing A-Z).
    *   Iterates through the plaintext vector in blocks of size `n`.
    *   For each block:
        *   Performs matrix multiplication between the `key_matrix` and the plaintext block vector.
        *   Applies the modulo 26 operation to the result of the matrix multiplication to ensure the ciphertext characters are within the range of A-Z.
        *   Converts the numerical results back to characters and appends them to the `ciphertext`.
