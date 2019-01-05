"""
From a sentence, deduce the total number of animals.
For example :
  "I see 3 zebras, 5 lions and 6 giraffes." The answer must be 14
  "Mom, 3 rhinoceros and 6 snakes come to us!" The answer must be 9
"""

"""
my difficulty here is to consider multiple consequetive integers when iterating over the string. I've used groupby to do this for now
"""

from itertools import groupby

count_animals = "in my zoo there are 16 goats, 4 dogs, 42 shrimp, 8 wolves. Thats it."

s = [int(''.join(i))
    for is_digit, i in groupby(count_animals, str.isdigit)
        if is_digit
    ]
    
print(sum(s))
