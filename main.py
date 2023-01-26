import random
from tkinter import *
from tkinter import ttk
from gui_ext import *

# Ce programme permet le chiffrement et déchiffrement de tous les caractères de l'alphabet latin minuscule
# Les spécifications de chaque méthode sont décrites dans README.md
# Les implémentations se trouvent dans le module ops.py


#Window init
root = Tk()
ttk.Label(root, text="NSIEncryption").grid(row=0)

ttk.Label(root, text="Message").grid(row=1)
ttk.Label(root, text="Key").grid(row=2)


message = ttk.Entry(root)
message.grid(row=1, column=1)

key = ttk.Entry(root)
key.grid(row=2, column=1)

methods = ['Cesar', 'ROT13', 'Vigenère', 'Polybius']
tk_method = StringVar(root)
tk_method.set(methods[0])

method = OptionMenu(root, tk_method, *methods)
method.grid(row = 10)

ttk.Button(root, text="Encrypt", command=lambda: compute(output, message, key, "Cesar")).grid(row=3)
output = ttk.Label(root, text="")
output.grid(row=4)

root.mainloop()