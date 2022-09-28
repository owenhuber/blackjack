from cProfile import run
import random
import threading
import queue
from helpahs import *
from countinghelpahs import * 

# One deck of cards
onedeck = []
for i in range(4):
    onedeck += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']

# a shuffle four decks of cards (standard shoe)
fourdeck = []
for i in range(4): 
    fourdeck += onedeck



# TODO figure out why this maxes out at 140ish and I cant replace with 'plastic'

def fourdeckplay(l) :
    '''simulates playing with four decks'''

    # shuffling
    random.shuffle(l)

    # The strategy that our player will follow can be found here https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

    q = queue.Queue()

    for val in l:
        q.put(val)

    # the card ('plastic') indicating when the dealer should stop
    plastic = random.randint(0, 208)

    # units won
    won = 0

    # the number of hands played
    games = 0

    # how many cards through
    count = 0

    # units gambled
    spent = 0

    while count < 120 : 

        # multiplier in case of double
        mult = 1

        spent += 1

        # getting our hands
        first = q.get()
        deal1 = q.get()
        sec = q.get()
        deal2 = q.get()
        hand = [first, sec]
        dealhand = [deal1, deal2]
        count += 4
        games += 1

        # check if we surrender first : if we do, we get back half of our bet and moved on to next hand
        if surrender(hand, deal1):
            won += 0.5
            continue

        # check if we can split : if should, carry on with each as hard counts TODO
        if cansplit(hand, deal1):

            # add another game played for cost 
            spent += 1

            # first run through with the hand 
            first1 = q.get()
            firsth = [first, first1]
            finfirst = hitting(firsth, deal1, q, count)

            # second run through with the hand TODO
            sec1 = q.get()
            sech = [sec, sec1]
            finsec = hitting(sech, deal1, q, count)

            # dealers final hand after hitting
            findeal = dealerhitting(dealhand, q, count)

            # every hands final count 
            firstnum = summ(finfirst)
            secnum = summ(finsec)
            dealnum = summ(findeal)

            # do you win the first hand ? 
            if push(firstnum, dealnum):
                won += 1
                continue
            if win(firstnum, dealnum):
                won += 2
                continue

            # do you win the second hand ? 
            if push(secnum, dealnum):
                won += 1
                continue
            if win(secnum, dealnum):
                won += 2
                continue
            continue


        if double(hand, deal1):
            # if we double and win, twice the payout. either way, twice the cost
            spent += 1
            # the third card that we are hit with
            third = q.get()
            count += 1

            # your hand's final value
            num1 = summ(hand) + summ([third])

            # dealers final hand after hitting
            deala = summ(dealerhitting(dealhand, q, count))

            # do you win the hand ? 
            if push(num1, deala):
                won += 2
                continue
            if win(num1, deala):
                won += 4
                continue
            continue

    
        # if none above applies, we can go back to base case
        myhand = hitting(hand, deal1, q, count)

        # dealers final hand after hitting
        dhand = dealerhitting(dealhand, q, count)

        # every hands final count 
        mynum = summ(myhand)
        dnum = summ(dhand)

        # do you win the hand ? 
        if push(mynum, dnum):
            won += 1*mult
            continue
        if win(mynum, dnum):
            won += 2*mult
            continue
    
    return won  / (won + spent)







# the strategy that we will be following for true counts can be found here : https://www.blackjackapprenticeship.com/how-to-count-cards/

def fourdeckcount1(l) :
    '''simulates playing with four decks and using the "true count"'''

    # shuffling
    random.shuffle(l)

    # The strategy that our player will follow can be found here https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

    qc1 = queue.Queue()

    for val in fourdeck:
        qc1.put(val)

    # the card ('plastic') indicating when the dealer should stop
    plastic = random.randint(0, 208)

    # our raw count 
    runningcount = 0

    # associated counts w each cards
    dicti = {2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 0, 8 : 0, 9 : 0, 10 : -1, 'A' : -1}

    # units won
    won = 0

    # the number of hands played
    games = 0

    # how many cards through
    count = 0

    # units gambled
    spent = 0

    while count < 120 : 

        # multiplier in case of double or strong deck
        mult = 1
        spent += 1

        if Truecount(runningcount, count) < -3 : 
            mult = 3
            spent += 2

    

        # getting our hands
        first = qc1.get()
        deal1 = qc1.get()
        sec = qc1.get()
        deal2 = qc1.get()
        hand = [first, sec]
        dealhand = [deal1, deal2]
        count += 4
        games += 1

        # adding these to our running count
        runningcount += dicti[first] + dicti[deal1] + dicti[sec] + dicti[deal2]

        # check if we surrender first : if we do, we get back half of our bet and moved on to next hand
        if surrender(hand, deal1):
            won += 0.5 * mult
            continue

        # check if we can split : if should, carry on with each as hard counts TODO
        if cansplit(hand, deal1):

            # add another game played for cost 
            spent += mult

            # first run through with the hand 
            first1 = qc1.get()
            firsth = [first, first1]
            finfirst = c1hitting(firsth, deal1, qc1, count, runningcount, dicti)

            # second run through with the hand TODO
            sec1 = qc1.get()
            sech = [sec, sec1]
            finsec = c1hitting(sech, deal1, qc1, count, runningcount, dicti)

            # dealers final hand after hitting
            findeal = c1dealerhitting(dealhand, qc1, count, runningcount, dicti)

            # every hands final count 
            firstnum = summ(finfirst)
            secnum = summ(finsec)
            dealnum = summ(findeal)

            # do you win the first hand ? 
            if push(firstnum, dealnum):
                won += mult
                continue
            if win(firstnum, dealnum):
                won += 2*mult
                continue

            # do you win the second hand ? 
            if push(secnum, dealnum):
                won += mult
                continue
            if win(secnum, dealnum):
                won += 2*mult
                continue
            continue


        if double(hand, deal1):
            # if we double and win, twice the payout. either way, twice the cost
            spent += mult
            # the third card that we are hit with
            third = qc1.get()
            count += 1

            # your hand's final value
            num1 = summ(hand) + summ([third])

            # dealers final hand after hitting
            deala = summ(c1dealerhitting(dealhand, qc1, count, runningcount, dicti))

            # do you win the hand ? 
            if push(num1, deala):
                won += 2*mult
                continue
            if win(num1, deala):
                won += 4*mult
                continue
            continue

    
        # if none above applies, we can go back to base case
        myhand = c1hitting(hand, deal1, qc1, count, runningcount, dicti)

        # dealers final hand after hitting
        dhand = c1dealerhitting(dealhand, qc1, count, runningcount, dicti)

        # every hands final count 
        mynum = summ(myhand)
        dnum = summ(dhand)

        # do you win the hand ? 
        if push(mynum, dnum):
            won += mult
            continue
        if win(mynum, dnum):
            won += 2*mult
            continue
    
    return won  / (won + spent)



#################################################################################################################################################
'''TESTING'''

# our average of winning percentage counting
notcounting = 0

# our average of winning percentage not counting
counting = 0

for i in range(1000) : 
    notcounting += fourdeckplay(fourdeck)
    counting += fourdeckcount1(fourdeck)

print(f'total win percentage not counting over 1000 shoes : {notcounting/ 1000}')
print(f'total win percentage counting over 1000 shoes : {counting/ 1000}')

