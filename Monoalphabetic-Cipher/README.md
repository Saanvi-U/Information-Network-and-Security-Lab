# Monoalphabetic Substitution Cipher in Python

This repository contains a Python implementation of a monoalphabetic substitution cipher. It demonstrates basic encryption and decryption using a fixed mapping of characters.

## Description

A monoalphabetic substitution cipher replaces each letter in the plaintext with the *same* corresponding letter in the ciphertext. This implementation uses a dictionary (`keys`) to define the substitution mapping. The `reverse_keys` dictionary is used for decryption.

The code includes two main functions:

* `encrypt(text)`: Encrypts the input text using the monoalphabetic substitution cipher. It handles both uppercase and lowercase letters. Non-alphabetic characters are left unchanged.
* `decipher(text)`: Decrypts the ciphertext back to plaintext using the reverse substitution mapping.

## How to Use

1.  You can run this code directly in Google Colab using the link provided below.

https://colab.research.google.com/drive/1qZbx4PPO7yBEd-rQ8ZGQYDbUzKrvf7jT?usp=sharing

## Example

Enter the plain text: Hello World!

Encrypted: itssg vgksr!

Decrypted: hello world!

## Code Explanation

The `keys` dictionary defines the substitution. For example, `keys['a'] = 'q'` means that the letter 'a' is *always* replaced by 'q' during encryption. The `reverse_keys` dictionary is the inverse of `keys`, allowing for decryption.

The `encrypt` and `decipher` functions iterate through the input text, substituting each character according to the dictionaries. The `get(char, char)` method is used to handle characters not found in the dictionaries (e.g., spaces, punctuation), leaving them unchanged.

