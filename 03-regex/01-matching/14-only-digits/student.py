# Write your code here
import re

def only_digits(string):
    return bool(re.fullmatch("[0-9]*", string))

string = "02857094823052304855234500342"

print(only_digits(string))