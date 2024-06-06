# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
    last_two_chars = str[-2:]
    return last_two_chars * 3

# Test cases
print(extra_end('Hello'))   # Output: lololo
print(extra_end('ab'))      # Output: ababab
print(extra_end('Hi'))      # Output: HiHiHi
