# Write your code here
import re

def one_or_more_abc(string):
    return bool(re.fullmatch("(abc)+", string))

string = "abcabcabcabc"

print(one_or_more_abc(string))