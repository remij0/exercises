# Write your code here
import re

def is_dna(string):
    return bool(re.fullmatch("[ACGT]*", string))

string = "AGTCGATCTCGACTCTGAGA"

print(is_dna(string))