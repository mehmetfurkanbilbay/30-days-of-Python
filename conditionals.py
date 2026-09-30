# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:12:40 2026

@author: furka
"""

# Conditionals

"""
 if condition:
   this part of code runs for truthy conditions
"""


a = 3

if a > 0:
    print('A is a positive number')
# A is a positive number   
    
"""
if condition:
    this part of code runs for truthy conditions
else:
    this part of code runs for false conditions

"""

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')


# If Elif Else

"""
# syntax
if condition:
    code
elif condition:
    code
else:
    code

"""


a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


# Short Hand

# code if condition else code

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed


# Nested Conditions
"""
if condition:
    code
    if condition:
    code

"""

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If Condition and Logical Operators

"""
if condition and condition:
    code
    
"""

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


# If and Or Logical Operators


"""
if condition or condition:
    code
"""

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')








