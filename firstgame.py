#!/usr/bin/env python3

print("Welcome to my first game")
name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 21:
    print("Hello, "+name+" You are elgible to play this game!")
else:
    print("Hello, "+name+" You are not elgible to play this game!")