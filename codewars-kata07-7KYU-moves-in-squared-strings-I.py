# This kata is the first of a sequence of four about "Squared Strings".
# You are given a string of n lines, each substring being n characters long: For example:
# s = "abcd\nefgh\nijkl\nmnop"

# We will study some transformations of this square of strings.

# Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
# vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
# Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
# hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"

# #Task:

# Write these two functions
# and

# high-order function oper(fct, s) where

# fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)
# #Examples:

# s = "abcd\nefgh\nijkl\nmnop"
# oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
# oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"


s = "abcd\nefgh\nijkl\nmnop"

def vert_mirror(strng):
    count = []
    strng = strng.splitlines()
    for st in strng:
        count.append(st[::-1])
        new_string = r'\n'.join(count)
    return new_string

def hor_mirror(strng):
    count = []
    strng = strng.splitlines()
    strng = strng[::-1]
    for st in strng:
        count.append(st[::1])
        new_string = r'\n'.join(count)
    return new_string

def oper(fct, s):
    print(fct(s))

oper(vert_mirror, s)
oper(hor_mirror, s)


# this should pass in codewars, it matches the exact output they want, but it doesn't pass. I need to figure out why.
