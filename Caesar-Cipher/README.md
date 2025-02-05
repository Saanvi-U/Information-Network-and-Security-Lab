
# Caesar Cipher Decryption

This repository provides a Python function for decrypting text encrypted using the Caesar cipher.  The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.  This code provides the decryption functionality, reversing the encryption process.

## Description

The `decryption(ciphertext, n)` function takes two arguments:

*   `ciphertext`: The encrypted text (string).
*   `n`: The shift value (integer) used for encryption. This is the number of positions each letter was shifted.

The function iterates through the ciphertext, decrypting each character:

*   Spaces are left unchanged.
*   Uppercase and lowercase letters are shifted back by `n` positions, wrapping around the alphabet if necessary (using the modulo operator `%`).
*   Non-alphabetic characters are also left unchanged.

The function returns the decrypted plaintext.

## How to Use


### Running in Google Colab:

1.  Click on the following link to open the code in Google Colab:

https://colab.research.google.com/github/Saanvi-U/Information-Network-and-Security-Lab/blob/main/Caesar_Cipher.ipynb

## Code Explanation

The `decryption(ciphertext, n)` function iterates through each character of the `ciphertext`:

1.  **Spaces:** If the character is a space, it's appended directly to the `plaintext`.
2.  **Uppercase Letters:** If the character is uppercase, it's shifted back by `n` positions using the formula `chr((ord(ch) - n - 65) % 26 + 65)`.  The modulo operator (`% 26`) ensures that the letters wrap around the alphabet (e.g., shifting 'A' back by 1 results in 'Z').
3.  **Lowercase Letters:** The same logic is applied to lowercase letters, using the appropriate ASCII offset (97 instead of 65).
4.  **Non-alphabetic Characters:** Any other character is appended directly to the `plaintext` without modification.






