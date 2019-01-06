"""
From a sentence, deduce the total number of animals.
For example :
  "I see 3 zebras, 5 lions and 6 giraffes." The answer must be 14
  "Mom, 3 rhinoceros and 6 snakes come to us!" The answer must be 9
"""

"""
my difficulty here is to consider multiple consequetive integers when iterating over the string. I googled groupby and pasted 
together some solutions to do this for now. I don't fully understand it"
"""

from itertools import groupby

count_animals = "in my zoo there are 16 goats, 4 dogs, 42 shrimp, 8 wolves. Thats it."

s = [int(''.join(i))
    for is_digit, i in groupby(count_animals, str.isdigit)
        if is_digit
    ]
    
print(sum(s))

"""
This was as far as I got on my own...

from itertools import groupby

def numbers(n):
    count = []
    for i in n:
        if i.isdigit():  #see what arguments this can take maybe to make whole numbers not single numbers
            count += i
    count = [int(i) for i in count] # turn the list from strings into int
    return sum(count)

print(numbers("there are 5 hippos, 50 beetles, 4 birds"))



# 2 problems. 1) how to add up shit in an array. 2) how to consider a number as multiple digits in a for loop

"""
