# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:27:05 2026

@author: furka
"""

# Loops

''' 
while condition:
    code goes here'''
    
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
    
'''
while condition:
    code goes here
else:
    code goes here
    '''
    
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
    

# Break and Continue - Part 1

"""
while condition:
    code goes here
    if another_condition:
        break
    """
    
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break 
    
    
'''
while condition:
    code goes here
    if another_condition:
        continue
'''

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
    

# For Loop\
    
'''
for iterator in lst:
    code goes here
    '''
    
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    
    

# Using For loop on string

'''
for iterator in string:
    code goes here
'''


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


# Using For loop on tuple

'''
for iterator in tpl:
    code goes here
    '''
    
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# For loop with dictionary

'''
for iterator in dct:
    code goes here
    '''
    
person = {
    'first_name':'John',
    'last_name':'Doe',
    'age':25,
    'country':'USA',
    'is_marred':True,
    'skills':['C', 'C++', 'Rust', 'Assembly', 'Python'],
    'address':{
        'street':'Broadway St',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# Using For Loop in set

'''
for iterator in st:
    code goes here
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    
    

# Break and Continue - Part 2

'''
for iterator in sequence:
    code goes here
    if condition:
        break
'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
    


# Continue

'''
for iterator in sequence:
    code goes here
    if condition:
        continue

'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


# The Range Function

lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

'''
for iterator in range(start, end, step):
    '''
    
for number in range(11):
    print(number)   # prints 0 to 10, not including 11


# Nested For Loop


'''
for x in y:
    for t in x:
        print(t)
'''


person = {
    'first_name':'John',
    'last_name':'Doe',
    'age':25,
    'country':'USA',
    'is_marred':True,
    'skills':['C', 'C++', 'Rust', 'Assembly', 'Python'],
    'address':{
        'street':'Broadway St',
        'zipcode':'02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

    

# For Else

'''
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
'''


for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
    
    
# Pass

for number in range(6):
    pass

