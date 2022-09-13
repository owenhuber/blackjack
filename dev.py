import numpy as np
import random
import threading
import queue
from chart import *

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
won = 0
count = 0

# The strategy that our player will follow can be found here https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

q = queue.Queue()
for val in fourdeck:
    q.put(val)

while count < plastic : 

    # getting our hand
    first = q.get()
    deal1 = q.get()
    sec = q.get()
    deal2 = q.get()
    hand = [first, sec]
    count += 4

    # check if we surrender first : if we do, we get back half of our bet and moved on to next hand
    if surrender(hand, deal1):
        won += 0.5
        continue

    # check if we can split : if should, carry on with each as hard counts TODO
    if cansplit(hand, deal1):
        first1 = q.git()
        firsth = [first, first1]
        if hit([first, first1], deal1):
            first2 = q.git()

        second1 = q.git()



# testing pipeline
