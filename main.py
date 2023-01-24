import random
from ops import *

# Ce programme permet le chiffrement et déchiffrement de tous les caractères de l'alphabet latin minuscule
# Les spécifications de chaque méthode sont décrites dans README.md
# Les implémentations se trouvent dans le module ops.py


# Tests
msgs = ["je m'appelle chaton", "@you, how are you doing?",
        "what's the point of doing this?"]
keys = [i**2 for i in range(5)] + [26, 27, 10, 13, 51, 100, 1028]

# Encrypts/Decrypts
encrypt = encrypt_polybius("Colon")
print(encrypt)
print(decrypt_polybius(encrypt))