```markdown
# Playfair Poly Cipher

Playfair Poly Cipher(Polyalphabetic Playfair cipher) is a Python library that provides tools for encrypting and decrypting text using the Playfair Cipher with a customizable key matrix.

## Installation

You can install Poly Playfair Cipher using pip:

```bash
pip install poly-playfair-cipher
```

## Example

### Encrypting Text

```python
from playfairpolycipher import PlayfairCipher

# Define a key for the Playfair Cipher
key = "KEYWORD"

# Initialize the PlayfairCipher with the key
cipher = PlayfairCipher(key)

# Encrypt a plaintext
plaintext = "HELLO WORLD"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)
```

### Decrypting Text

```python
from playfairpolycipher import PlayfairCipher

# Define a key for the Playfair Cipher
key = "KEYWORD"

# Initialize the PlayfairCipher with the key
cipher = PlayfairCipher(key)

# Decrypt a ciphertext
ciphertext = "ILIDGJZTJG"
plaintext = cipher.decrypt(ciphertext)
print("Decrypted Text:", plaintext)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```