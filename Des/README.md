# DES Key Generation  

This program implements a simple DES-like key generation process by taking an input string, converting it to binary, and applying a custom permutation and shifting technique to generate multiple keys.  

## Features  
- Converts input text to binary representation.  
- Applies a bitwise permutation and shift operation.  
- Generates 8 unique keys based on transformations.  

## How It Works  
1. The input string is converted into an 8-bit binary format.  
2. The first bit of each byte is removed to create a new binary string.  
3. The binary string is split into left and right halves.  
4. A predefined permutation (lt array) is used to shift each half.  
5. The shifted halves are combined and random bits are removed to create unique keys.  
6. The program outputs 8 different keys.  

## How to Run  
### Google Colab link: 
https://colab.research.google.com/github/Saanvi-U/Information-Network-and-Security-Lab/blob/main/des.ipynb#scrollTo=OTSdSbKyqsRG

### Run Locally  
1. Install Python 3.x if not installed.  
2. Copy the script into a Python file (`des_keygen.py`).  
3. Run the script:  
   ```bash
   python des_keygen.py
