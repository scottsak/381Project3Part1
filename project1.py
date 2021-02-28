'''
EE 281 Project 1 - Part 1
Scott Sakurai
018497139
'''
import random

p = float(input('Enter the probability of success: '))
T = int(input('Enter the probability of trials: '))

for i in range(T):
    r = random.uniform(0,1)

    if r<p:
        print('1', end='')
    else:
        print('0',end='')