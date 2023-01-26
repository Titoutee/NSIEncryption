from tkinter import *
from tkinter import ttk
from ops import *

def compute(label, message_entry, key_entry, method):
    '''Détermine la string chiffrée ou déchiffrée et l'affiche'''
    message, key = message_entry.get(), key_entry.get()
    label.config(text=f"{encrypt_cesar(message, (int(key) if key and key.isnumeric() else 0))}")