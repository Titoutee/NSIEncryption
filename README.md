# Spécifications de chaque méthode

# Les 3 premières méthodes consistent en un déplacement de caractères dans l'alphabet:


# Code de César: 
# -déplacer chaque lettre de "clé" lettres


# ROT13:
# -version spécial du Code de César, avc une clé prédéfinie égale à 13


# Code de Vigenère:
# -la clé est une chaîne de caractères au lieu d'un nombre
# -on déplace chaque lettre du message par le code ASCII de la lettre correspondante dans la clé
# -si le message et la clé ne sont pas de taille égale, soit on boucle sur la clé, soit certains caractères de la clé resteront inutilisés


# Carré de Polybe:
# -établir une matrice (ou une abstraction comme faite, avec un calcul d'indice) comportant tous les caractères de l'alphabet latin minuscule, en ommettant la lettre 'j' par convention, pour obtenir un carré (26-1=25 lettres). La lettre 'i' compte donc pour deux
# -chaque lettre du message est chiffré en donnant ses coordonnées dans la liste de caractères (matrice "virtuelle" dans mon implémentation)

# Chacune des méthodes n'opère que sur l'alphabet latin

# Fichiers:
# -ops.py: implémentations des fonctions de chiffrement et déchiffrement de chaque méthode
# -utils.py: fonctions diverses
# -gui_ext.py: fonctions externes servant pour la création de l'interface graphique
