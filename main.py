import random
from tkinter import *
from tkinter import ttk
from gui_ext import *

# Ce programme permet le chiffrement et déchiffrement de tous les caractères de l'alphabet latin minuscule
# Les spécifications de chaque méthode sont décrites dans README.md
# Les implémentations se trouvent dans le module ops.py


#Fenêtre titrée
root = Tk()
ttk.Label(root, text="NSIEncryption").grid(row=0)

ttk.Label(root, text="Message").grid(row=1)
ttk.Label(root, text="Key").grid(row=2)

# Zone de saisie du message
message = ttk.Entry(root)
message.grid(row=1, column=1)

# Zone de saisie de la clé (0 si non renseignée ou si non numérique)
key = ttk.Entry(root)
key.grid(row=2, column=1)

# Menu déroulant des méthodes
methods = ['Cesar', 'ROT13', 'Vigenere', 'Polybius']
tk_method = StringVar()
tk_method.set(methods[0])
method = OptionMenu(root, tk_method, *methods)
method.grid(row = 10)

# Menu déroulant des actions (chiffrer/déchiffrer)
actions = ['Encrypt', 'Decrypt']
tk_action = StringVar()
tk_action.set(actions[0])
action = OptionMenu(root, tk_action, *actions)
action.grid()

# Bouton d'action (chiffrer/déchiffrer)
ttk.Button(root, text="Encrypt", command=lambda: compute(output, message, key, tk_method, tk_action)).grid(row=3)

# Résultat
output = ttk.Label(root, text="")
output.grid(row=4)

ttk.Button(root, text="Quit", command=root.destroy).grid(sticky="s")

root.mainloop()