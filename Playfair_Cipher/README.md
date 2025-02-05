# Playfair Cipher in Python

This repository contains a Python implementation of the Playfair cipher. It demonstrates encryption using a key-based substitution method.

## Description

The Playfair cipher is a manual symmetric encryption technique that encrypts digraphs (pairs of letters) instead of single letters. It uses a 5x5 key square containing a keyword mixed with the remaining letters of the alphabet.

This implementation handles the following:

*   Key preparation: The key is processed to remove duplicate letters and the letter 'J' (which is replaced by 'I').
*   Message preparation: The message is converted to uppercase and 'J's are replaced with 'I's.  Pairs of letters are created. If a pair has identical letters, an 'X' is inserted between them. If the message has an odd number of letters, an 'X' is appended.
*   Encryption: The digraphs are encrypted based on their position in the key square, following specific rules (same row, same column, rectangle).

## How to Use

1.  You can run this code directly in Google Colab using the link provided below.

   https://colab.research.google.com/drive/10NKw99KtwZIRlDS2fKbcHrwJn9bAUOlY?usp=sharing

## Example

Enter the key: keyword

Enter the message: Hello World

Encrypted: KIYHSXODZRU

## Code Explanation

1.  **Key Preparation:** The `key` is processed to remove duplicate letters and 'J's.  The remaining letters of the alphabet (excluding 'J') are appended to the key.  This creates the 5x5 key square (`table`).

2.  **Message Preparation:** The `message` is converted to uppercase and 'J's are replaced with 'I's. The message is then broken into digraphs (pairs of letters).  If two letters in a pair are the same, an 'X' is inserted between them. If the message has an odd number of letters, an 'X' is appended to make the last pair.

3.  **Encryption:** The `encrypt(pair)` function encrypts each digraph based on the rules of the Playfair cipher:
    *   **Same Row:** If the letters are in the same row, they are replaced by the letters to their immediate right (wrapping around).
    *   **Same Column:** If the letters are in the same column, they are replaced by the letters immediately below them (wrapping around).
    *   **Rectangle:** If the letters form a rectangle, they are replaced by the letters in the same row but at the other corner of the rectangle.
