
import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
prac = [4, 12]
v = 4

#if 3 < v < 5 :
#    print('FUCK YEA')

l = ['A', 2]

val = [e for e in l if isinstance(e, int)][0]

n = 1

while n < 20: 
    n += 1
    if n % 3 == 0 : 
        continue




# One deck of cards
onedeck = []
for i in range(4):
    onedeck += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']

# a shuffle four decks of cards (standard shoe)
fourdeck = []
for i in range(4): 
    fourdeck += onedeck

# shuffling
random.shuffle(fourdeck)



dictionary = {1: 2, 3 : 6}

s = '12345'

for i in range(1, len(s) + 1):
    print(s[-i])


# write your code in Python 3.6

    # getting our dictionary of connections
    dicti = {}
    for i in range(len(A)):
        if dicti.has_key(A[i]) : 
            dicti[A[i]].append(B[i])
        else : 
            dicti[A[i]] = [B[i]]
        if dicti.has_key(B[i]):
                dicti[B[i]].append(A[i])
        else : 
            dicti[B[i]] = [A[i]]

    secs = 0

    popped = []

    dictib = dicti

    while len(dicti) > 0 : 
        for key in dicti : 
            if len(dicti[key]) == 1 : 
                del dictib[key]
        dicti = dictib
        secs += 1


