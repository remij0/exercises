# Write your code here
import re

def one_or_more_a(string):
    return bool(re.fullmatch("a+", string))

string = "aaaa"

print(one_or_more_a(string))