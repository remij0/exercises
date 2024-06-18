# Write your code here
import re

def only_letters(string):
    return bool(re.fullmatch("[a-zA-z]*", string))

string = "fjlasKJIDSksaKAIdkAkdAKsdLAd"

print(only_letters(string))