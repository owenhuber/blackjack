'''Standard chart of what to do in different circumstances'''

def surrender(l, d):
    '''first : should you surrender?'''
    if 12 in l :
        return False
    if sum(l) == 16 and d > 8 :
        return True
    if sum(l) == 15 and d == 10 : 
        return True
    return False

def cansplit(l, d) : 
    '''second : should you split?'''
    # TODO double after split implement
    if l[0] != l[1] or l[0] == 10 or l[0] == 5:
        return False
    if l[0] == 12 or l[0] == 8 : 
        return True
    if l[0] == 9 :
        if d < 10 and d != 7 :
            return True
    if l[0] == 7 and d < 8 : 
        return True
    if l[0] == 6 and d < 7 : 
        return True
    if l[0] == 4 : 
        if d == 5 or d == 6 :
            return True
    if l[0] == 3 or l[0] == 2 : 
        if d < 8 : 
            return True
    return False

def double(l, d) : 
    '''third : Should you double'''
    l = sorted(l)
    if l[1] == 12 : 
        if d == 6 and l[0] < 9 :
            return True
        if d == 5 and l[0] < 8 :
            return True
        if d == 4 and 3 < l[0] < 8 :
            return True
        if d == 4 and 3 < l[0] < 8 :
            return True
        if d == 3 and 5 < l[0] < 8 :
            return True
        if d == 2 and l[0] == 7 :
            return True
        return False
    if sum(l) == 11 : 
        return True
    if sum(l) == 10 and d < 10 : 
        return True
    if sum(l) == 9 and 2 < d < 7 : 
        return True
    return False

def hit(l, d): 
    '''third : should you hit?'''
    hard = sum(l)
    if hard > 16 : 
        return False
    if d > 6 : 
        return True
    if hard < 12 : 
        return True
    if hard == 12 and d < 4 : 
        return True
    return False