# Write your code here
import re

def is_number(string):
    return bool(re.fullmatch("[0-9]+", string))

string = "572093480523"

print(is_number(string))