def without(l, pred):
    '''Retourne l en retirant pred (première occurence)
    # l doit être non-vide et doit contenir pred au moins une fois'''
    res = l.copy()
    res.remove(pred)
    return res