# Write an algorithm that takes an array and moves all of the zeros
# to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    return [nz for nz in lst if nz != 0] + [z for z in lst if z == 0]
