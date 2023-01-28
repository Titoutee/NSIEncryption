from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ops import *

def compute(label, message_entry, key_entry, method_option, action_option):
    '''Détermine la string chiffrée ou déchiffrée et l'affiche'''
    msg, key = message_entry.get(), key_entry.get()
    method, action = method_option.get(), action_option.get()
    label.config(text=f"{(encrypt_compute(method_option.get(), msg, key) if action == 'Encrypt' else decrypt_compute(method, msg, key))}")
    
def encrypt_compute(method, msg, key):
    if method == "Cesar":
        return encrypt_cesar(msg, (int(key) if key and key.isnumeric() else 0))
    elif method == "ROT13":
        return encrypt_ROT13(msg)
    elif method == "Vigenere":
        return encrypt_vigenere(msg, key if key else " ")
    return encrypt_polybius(msg)

def decrypt_compute(method, msg, key):
    if method == "Cesar":
        return decrypt_cesar(msg, (int(key) if key and key.isnumeric() else 0))
    elif method == "ROT13":
        return decrypt_ROT13(msg)
    elif method == "Vigenere":
        return decrypt_vigenere(msg, key if key else " ")
    return decrypt_polybius(msg)
def info():
    messagebox.showinfo(title="Infos", message="Message empty -> empty result/Key empty -> Default to 0 if Cesar, default to SPACE if Vigenere")