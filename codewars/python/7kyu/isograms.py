# An isogram is a word that has no repeating letters,
# consecutive or non-consecutive. Implement a function that determines
# whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

# def is_isogram(string):
#     #your code here

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    return len(string) == len(set(string.lower()))
