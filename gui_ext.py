from tkinter import *
from tkinter import ttk
from ops import *

def compute(label, message_entry, key_entry, method_option, action_option):
    '''Détermine la string chiffrée ou déchiffrée et l'affiche'''
    msg, key = message_entry.get(), key_entry.get()
    label.config(text=f"{method_comp(method_option.get(), msg, key)}")
    
def method_comp(method, msg, key):
    if method == "Cesar":
        return encrypt_cesar(msg, (int(key) if key and key.isnumeric() else 0))
    elif method == "ROT13":
        return encrypt_ROT13(msg)
    elif method == "Vigenere":
        return encrypt_vigenere(msg, key)
    return encrypt_polybius(msg)