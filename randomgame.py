#!/usr/bin/env python3

#This is a guess the number game

import random

print ('Hello. What is your name?')
name = input()

print('Well, '+name+', I am thinking of a number between 1 and 20.')
SecretNumber = random.randint(1,20)

for guesstaken in range(1,2): 
    print('Take a guess idiot')
guess = int(input())
if guess < SecretNumber:
    print('Your guess is too low.')
elif guess > SecretNumber:
    print('Your guess is too high.')
if guess == SecretNumber:
    print('Good job, ' +name+ '! You guessed my number in ' +str(guesstaken)+'guesses.')
else:
    print('Nope. The number I was thinking of is ' + str(SecretNumber))