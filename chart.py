'''Standard chart of what to do in different circumstances'''

def notace(l):
    '''returns integer in list that may include string '''
    if len(l) == 2 : 
        return [e for e in l if isinstance(e, int)][0]
    return [e for e in l if isinstance(e, int)]

def surrender(l, d):
    '''first : should you surrender?'''
    if 'A' in l :
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
    if l[0] == 'A' or l[0] == 8 : 
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
    if 'A' in l: 
        val = notace(l)
        if d == 6 and val < 9 :
            return True
        if d == 5 and val < 8 :
            return True
        if d == 4 and 3 < val < 8 :
            return True
        if d == 4 and 3 < val < 8 :
            return True
        if d == 3 and 5 < val < 8 :
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

    if 'A' in l :
        # tests out should use Ace as 1 or 11, and accordingly if should hit
        if len(l) == 2 : 
            hard1 = [notace(l) + 1, 0]
            hard2 = [notace(l) + 11, 0]
        else : 
            hard1 = [sum(notace(l)) + 1, 0]
            hard2 = [sum(notace(l)) + 11, 0]
        if hit(hard1, d) or hit(hard2, d):
            return True
    
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