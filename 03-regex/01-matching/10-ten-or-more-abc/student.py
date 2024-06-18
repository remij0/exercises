# Write your code here
import re

def ten_or_more(string):
    return bool(re.fullmatch("(abc){10,}", string))

string = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"

print(ten_or_more(string))