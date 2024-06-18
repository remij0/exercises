# Write your code here
import re

def is_valid_student(string):
    return bool(re.fullmatch("[srSR][0-9]{7}", string))

string = "r1234567"

print(is_valid_student(string))

string = "s1234567"

print(is_valid_student(string))

string = "R7654321"

print(is_valid_student(string))

string = "S4857692"

print(is_valid_student(string))