import numpy as np
import random
import threading
import queue
from chart import *

# One deck of cards
# 12 is an Ace
onedeck = []
for i in range(4):
    onedeck += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 12]

# a shuffle four decks of cards (standard shoe)
fourdeck = []
for i in range(4): 
    fourdeck += onedeck

# the card ('plastic') indicating when the dealer should stop
plastic = random.randint(0, 208)
count = 0

# The strategy that our player will follow can be found here https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

q = queue.Queue()
for val in fourdeck:
    q.put(val)

while count < plastic : 
    first = q.get()
    deal1 = q.get()
    sec = q.get()
    deal2 = q.get()
    count += 4


