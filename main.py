import string as string_mod
import random

# Nombre de lettres dans l'alphabet
ALPH_CHAR_NB = 26
# L'addresse de la première lettre minuscule de l'alphabet latin dans la table ASCII
ALPH_LOWER_ASCII_BEG = 97

# Liste de toutes les lettres de l'alphabet latin minuscule (module "string")
alph = list(string_mod.ascii_lowercase)


# Ce programme permet le chiffrement et déchiffrement de tous les caractères de l'alphabet latin minuscule
# Les spécifications de chaque méthode sont décrites dans README.md


def decal_int(msg, key):  # Fonction de base pour les trois premières méthodes
    '''Fonction de base du code de César, ROT13 et Code de Vigenère.
    Retourne le message en entrée, mais chiffré selon "key".
    Chaque lettre est décalée de "key".'''
    string = ""  # string de retour
    for letter in msg.lower():  # les majuscules deviennent minuscules
        encrypt = chr((ord(letter)+key-ALPH_LOWER_ASCII_BEG) % ALPH_CHAR_NB +
                      ALPH_LOWER_ASCII_BEG)  # Le caractère chiffré à l'aide de la clé
        # on ajoute la lettre chiffrée à la string de retour
        # les caractères non présents dans "alph" restent tels quels dans le message chiffré
        string = string + (encrypt if letter in alph else letter)
    return string

# Code de César


def encrypt_cesar(msg, key):
    '''Renvoie "msg" chiffré à l'aide de la méthode du code de césar (si msg vide le msg chiffré est vide)'''
    return decal_int(msg, key)


def decrypt_cesar(msg, key):
    '''Renvoie "msg" déchiffré à l'aide de la méthode du code de césar (si msg vide le msg déchiffré est vide)'''
    return decal_int(msg, -key)  # Opposé de la clé

# ROT13


ROT13_KEY = 13  # Clé de chiffrement de la méthode ROT13 (constante)


def encrypt_ROT13(msg):
    ''' Renvoie "msg" chiffré à l'aide de la méthode de ROT13 (si msg vide le msg chiffré est vide)'''
    return decal_int(msg, ROT13_KEY)


def decrypt_ROT13(msg):
    '''Renvoie "msg" déchiffré à l'aide de la méthode de ROT13 (si msg vide le msg déchiffré est vide)'''
    return decal_int(msg, -ROT13_KEY)  # Opposé de la clé

# Code de Vigenère


def encrypt_vigenere(msg, key):
    '''Renvoie "msg" chiffré à l'aide de la méthode du Code de Vigenère (si msg vide le msg chiffré est vide)'''
    string = ""
    a = 0
    # Pas besoin de `.lower()`, chaque lettre deviendra minuscule dans `decal_int()`
    for i in msg:
        # On boucle sur la clé si la clé est plus courte que le message à chiffrer
        string = string + decal_int(i, ord(key[a % len(key)]))
        a += 1
    return string


def decrypt_vigenere(msg, key):
    '''Renvoie "msg" déchiffré à l'aide de la méthode du Code de Vigenère (si msg vide le msg chiffré est vide)'''
    string = ""
    a = 0
    # Pas besoin de `.lower()`, chaque lettre deviendra minuscule dans `decal_int()`
    for i in msg:
        string = string + decal_int(i, -ord(key[a % len(key)]))  # Clé opposée
        a += 1
    return string


# Polybe



def without(l, pred):
    '''Retourne l en retirant pred (première occurence)'''
    res = l.copy()
    res.remove(pred)
    return res


# Crée une nouvelle liste à partir de "alph" en excluant 'i'
pred, rep = 'i', 'j' # 'i' et 'j' sont fusionnés dans le carré de polybe
polybian = without(alph, 'i')
sub_length = 5


def encrypt_polybian(msg, polybian=polybian, pred=pred, rep=rep):
    '''Renvoie "msg" chiffré à l'aide de la méthode du Code de Vigenère (si msg vide le msg chiffré est vide)
    Si `msg` contient des caractères ne faisant pas partie de `alph`, ceux-ci ne seront pas chiffrés'''

    
    res = ""  # Séquence finale de coordonnées dans le carré de Polybe
    space = False
    for char in msg.lower():  # Message en minuscule
        # Pred et rep (par défaut 'i' et 'j') sont fusionnés dans le carré
        if char == pred:
            char = rep
        space = (char == ' ')
        if char in polybian:  # On ne chiffre aucun caractère qui n'appartienne pas à l'alphabet restreint
            # accède à l'indice du caratcère dans polybian
            index = polybian.index(char)
        # Ajout des coordonnées du caractère à la string de retour
        res = res + f"{index//sub_length}{index%sub_length}{'|' if space else ' '}"
    return res


def decrypt_polybian(encrypted):
    res = ""
    for word in encrypted.split('|'):
        for coords in word.split():  
            x, y = coords
            res = res + polybian[int(x)*sub_length + int(y)]
    
    return res



# Tests
msgs = ["je m'appelle chaton", "@you, how are you doing?",
        "what's the point of doing this?"]
keys = [i**2 for i in range(5)] + [26, 27, 10, 13, 51, 100, 1028]

# Encrypts/Decrypts
print(without(alph, 'i'))
encrypt = encrypt_polybian("cereales avec lait")
print(encrypt)
print(decrypt_polybian(encrypt))