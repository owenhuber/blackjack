import numpy as np
import random
import threading
import queue
from helpahs import *

# One deck of cards
# 12 is an Ace
onedeck = []
for i in range(4):
    onedeck += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']

# a shuffle four decks of cards (standard shoe)
fourdeck = []
for i in range(4): 
    fourdeck += onedeck

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

# The strategy that our player will follow can be found here https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

q = queue.Queue()
for val in fourdeck:
    q.put(val)


while count < plastic : 

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
        first1 = q.git()
        firsth = [first, first1]
        finfirst = hitting(sech, deal1, q, count)

        # second run through with the hand TODO
        sec1 = q.git()
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


    if double(hand, deal1):
        # if we double and win, twice the payout. either way, twice the cost
        spent += 1
        mult = 2
    
    # if none above applies, we can go back to base case
    myhand = hitting(hand, deal1, q, count)

    # dealers final hand after hitting
    dhand = dealerhitting(dealhand, q, count)

    # every hands final count 
    mynum = summ(myhand)
    dnum = summ(dhand)

    # do you win the hand ? 
    if push(mynum, dnum):
        won += 1
        continue
    if win(mynum, dnum):
        won += 2
        continue


        

