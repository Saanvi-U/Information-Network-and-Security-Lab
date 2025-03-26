# Secure Key Management System (KMS)

## Overview
The **Secure Key Management System (KMS)** is a Python-based implementation of cryptographic tools for secure key generation, encryption, and management. It supports:
- **AES**: Symmetric encryption for secure data handling.
- **RSA**: Asymmetric encryption for secure communication.
- **Diffie-Hellman**: Ephemeral key exchange for forward secrecy.
- Key revocation and centralized management.

This system is designed with strong security measures, including protection against Man-in-the-Middle (MITM) attacks, forward secrecy, and key lifecycle management.

---

## Features
- **AES Encryption/Decryption**:
  Generate AES keys and securely encrypt/decrypt data.
- **RSA Key Pair Management**:
  Generate RSA key pairs for secure asymmetric encryption and decryption.
- **Diffie-Hellman Key Exchange**:
  Create ephemeral keys for secure session communication.
- **Key Revocation**:
  Easily revoke compromised keys.
- **Secure Logging**:
  All critical operations are logged for traceability.

---

## How to Run
### Google Colab Demo
To see a demonstration of the Secure Key Management System, use the following Google Colab link:

https://colab.research.google.com/drive/1mRHzNOcHKGMMuE44m8x9uL1ecNpafLdJ?usp=sharing

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python kms_code.py
   ```

4. Key Functionalities:
   - Generate AES keys and encrypt/decrypt sensitive data.
   - Create and use RSA key pairs for secure communication.
   - Use Diffie-Hellman for key exchanges with forward secrecy.
   - Revoke compromised keys securely.

---

## Prerequisites
To run the project locally, ensure you have:
1. **Python 3.7 or later** installed.
2. The `cryptography` library installed. You can install it with:
   ```bash
   pip install cryptography
   ```

---


## Security Considerations
1. **Preventing MITM Attacks**:
   - RSA public keys would ideally be distributed through a trusted PKI.
   - Use TLS or other secure communication channels in production.

2. **Forward Secrecy**:
   - Diffie-Hellman ephemeral keys ensure that past communications remain secure.

3. **Key Revocation**:
   - Centralized storage of keys simplifies revocation and management.

