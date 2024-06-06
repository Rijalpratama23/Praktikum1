# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
    return a + b + b + a

# Test cases
print(make_abba('Hi', 'Bye'))       # Output: HiByeByeHi
print(make_abba('Yo', 'Alice'))     # Output: YoAliceAliceYo
print(make_abba('What', 'Up'))      # Output: WhatUpUpWhat
