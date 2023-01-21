import argparse
import string as string_mod
import random

ALPH_CHAR_NB = 26  # Nombre de lettres dans l'alphabet
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


def without(arr, pred):
    '''Renvoie l'array en enlevant préalablement `pred`'''
    if pred not in arr:
        raise ValueError  # Si pred n'est pas dans l'array, alors on ne peut pas l'enlever
    a = alph
    a.remove(pred)
    return a

def filter(arr, register = alph):
    '''Supprime de `arr` tout élément qui ne fait pas partie de `register`'''
    for i in arr:
        if i not in register:
            arr.remove(i)

def encrypt_polybe(msg, l):
    '''Renvoie "msg" chiffré à l'aide de la méthode du Code de Vigenère (si msg vide le msg chiffré est vide)
    Si `msg` contient des caractères ne faisant pas partie de `alph`, ceux-ci sont retirés (le principe de la méthode oblige)'''
    
    filter(msg, alph) # On enlève de `msg` chaque lettre qui ne fait pas partie de `alph` (pour s'éviter des validations par la suite)
    
    # Si la lettre que l'on souhaite retirer n'est pas dans `alph`, alors on prend `alph` tout entier
    # (cas en réalité improbable, car l'on sait que `j` est dans l'alphabet latin minuscule)
    polybian_alph = without(alph, )
    string = ""
    for i in msg.lower():
        # Pas besoin ici de catch une potentielle exception 
        index = alph.index(i)
        string = string + (f"{len(polybian_alph)//l}{polybian_alph}")


# Tests
msgs = ["je m'appelle chaton", "@you, how are you doing?",
        "what's the point of doing this?"]
keys = [i**2 for i in range(5)] + [26, 27, 10, 13, 51, 100, 1028]

# Encrypts/Decrypts
print(encrypt_polybe("Hey"))
encrypt = encrypt_vigenere("Je m'appelle Tristan", "Yolo 21!@")
print(encrypt)
print(decrypt_vigenere(encrypt, "Yolo 21!"))