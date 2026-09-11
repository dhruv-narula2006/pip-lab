# Program File: exp_15b.py
from exp_15a import casual_greeting, formal_greeting, friendly_greeting

name = input("Enter your name: ")
print("Greeting Casually:  " + casual_greeting(name))
print("Greeting Formally:  " + formal_greeting(name))
print("Greeting Friendly:  " + friendly_greeting(name))