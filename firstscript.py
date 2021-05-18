#!/usr/bin/env python3
#This program says hello and asks for my name 

print('Hello World!')
print('What is your name?') #ask for thier name 
myName= raw_input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #ask for thier age 
myAge= raw_input()
print('You will be ' + str(int(myAge) + 1) + ' in the year 2020. Happy New Year!!!!')