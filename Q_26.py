# Program to Shuffle deck of cards (Using random and itertools modules)

import random,itertools

deck  = list(itertools.product(range(1,14),["Spade","Club","Hearts","Diamond"]))

random.shuffle(deck)
for i in range(5):
    print(deck[i][0] , "of",deck[i][1])

