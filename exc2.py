# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.
# Use the characters exactly once
import math
import random
char_list = ['a', 'e', 'i', 'o', 'u']
list_of_words = []
count = 0
elements = len(char_list)

# Need to add better calculation to factor that some elements can be repeated and it decreases unique count 
max_combination = math.factorial(elements)
print("max combination: ", max_combination)

while True:
    random.shuffle(char_list)
    new = ''.join(char_list)
    if new in list_of_words:
        pass
    else:
        list_of_words.append(new)
        print(new)
        count += 1
        if count == max_combination:
            break



