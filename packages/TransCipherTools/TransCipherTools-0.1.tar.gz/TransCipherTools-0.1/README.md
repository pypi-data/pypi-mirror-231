```markdown
# TranspositionCipher

TranspositionCipher is a Python library that provides tools for encrypting and decrypting text using the Railfence and Columnar cipher.

## Installation

You can install using pip:

```bash
pip install TransCipherTools
```

## Example

### Encrypting & Decrypting using Railfence cipher

```python
from TransCipherTools import railfence
encrypted_text = railfence.encrypt(msg,no_of_rails) # eg. ("Hello",2)
decrypted_text = railfence.decrypt(cipher,no_of_rails)
```

### Encrypting & Decrypting using Columnar cipher 

```python
from TransCipherTools import columnar
encrypted_text =columnar.encrypt_message(msg, key)
decrypted_text = columnar.decrypt_message(cipher, key)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```