'''Standard chart of what to do in different circumstances'''

def notace(l):
    '''returns integer in list that may include string '''
    if len(l) == 2 : 
        return [e for e in l if isinstance(e, int)]
    return [e for e in l if isinstance(e, int)]

def surrender(l, d):
    '''first : should you surrender?'''
    if 'A' in l :
        return False
    if sum(l) == 16 and (d == 'A' or d > 8 ):
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
    if d == 'A' : 
        if l[0] == 'A' or l[0] == 8 :
            return True
        return False
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
        if d == 'A' : 
            return False
        val = notace(l)[0]
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
    if d == 'A' and sum(l) != 11 : 
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
        hard1 = [sum(notace(l)) + 1, 0]
        hard2 = [sum(notace(l)) + 11, 0]
        if hit(hard1, d) or hit(hard2, d):
            return True
        return False
    
    hard = sum(l)
    if hard > 16 : 
        return False
    if d == 'A' or d > 6 : 
        return True
    if hard < 12 : 
        return True
    if hard == 12 and d < 4 : 
        return True
    return False


def hitting(l, d, qu, coun):
    '''process for hitting, returns final hand'''

    # if you aren't hitting, return that hand
    if not hit(l, d):
        return l
    
    # if you are hitting...
    l.append(qu.get())
    coun += 1
    return hitting(l, d, qu, coun)
    

def summ(l) : 
    '''allows us to evaluate the sum of a hand with aces too, returns higher one if having 11 doesnt make bust'''
    if 'A' not in l : 
        return sum(l)
    before = sum(notace(l))
    if before < 11 : 
        return before + 11
    return before + 1


def dealerhitting(dealh, qu, coun): 
    # dealer must stop! stop I say, stop!
    if summ(dealh) > 16 : 
        return dealh
    
    # if you must keep hitting...
    dealh.append(qu.get())
    coun += 1
    return dealerhitting(dealh, qu, coun)


    
def push(you, deal) : 
    '''do you push with the dealer?'''
    if you > 21 : 
        return False
    if you == deal : 
        return True
    return False

def win(you, deal) : 
    '''do you win vs the dealer?'''
    if you > 21 : 
        return False
    if deal > 21 : 
        return True
    if you > deal : 
        return True
    return False

