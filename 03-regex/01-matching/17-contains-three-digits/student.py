
# Write your code here
import re

def contains_three_digits(string):
    return bool(re.fullmatch(".*[0-9].*[0-9].*[0-9]", string))

string = "a1b2c3"

print (contains_three_digits(string))