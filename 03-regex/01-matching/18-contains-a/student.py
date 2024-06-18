# Write your code here
import re

def contains_a(string):
    return bool(re.search("a", string))

string = "a484a82a34gsljdfglsad"

print(contains_a(string))