
def decksleft(count) : 
    '''inputs queue, returns how many decks are left in the shoe'''
    return (208 - count) / 52

def Truecount(rawc, count) : 
    '''the true count'''
    return rawc / decksleft(count)

def notace(l):
    '''returns integer in list that may include string '''
    if len(l) == 2 : 
        return [e for e in l if isinstance(e, int)]
    return [e for e in l if isinstance(e, int)]

def summ(l) : 
    '''allows us to evaluate the sum of a hand with aces too, returns higher one if having 11 doesnt make bust'''
    if 'A' not in l : 
        return sum(l)
    before = sum(notace(l))
    if before < 11 : 
        return before + 11
    return before + 1


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



def c1hitting(l, d, qu, coun, rawc, diction):
    '''process for hitting, returns final hand'''

    # if you aren't hitting, return that hand
    if not hit(l, d):
        return l
    
    # if you are hitting...
    val = qu.get()
    l.append(val)
    coun += 1

    rawc += diction[val]

    return c1hitting(l, d, qu, coun, rawc, diction)
    



def c1dealerhitting(dealh, qu, coun, rawc, diction): 
    '''dealer playing while counting'''
    # dealer must stop! stop I say, stop!
    if summ(dealh) > 16 : 
        return dealh
    
    # if you must keep hitting...
    val = qu.get()
    dealh.append(val)
    coun += 1
    rawc += diction[val]
    return c1dealerhitting(dealh, qu, coun, rawc, diction)