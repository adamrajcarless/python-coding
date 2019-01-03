from collections import Counter  # because this python module already does the job

def duplicate_encode(word):
    new_string = ''  # establishing the new string
    word = word.lower()  # forcing the passed in string to be lowercase
    c = Counter(word)  # using the Counter module to work out no.of dupes in the function argument, stored as the var, c
    for letter in word:  # for loop iterating over each letter in the word
        if c[letter] == 1  # if the letter exists just the once
            letter = ')' # then letter becomes the string ')'
        else: 
            letter = '('  # but if anything else i.e. multiple, then the string '('
        new_string = new_string + letter  # here we append the content of the letter variable to the new_string variable
    return new_string  # here we define the output of this function, the contents of the new_string variable

print(duplicate_encode('recede')  # this is the function call, passing in the string 'recede' as its argument
