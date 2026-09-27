# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:56:12 2026

@author: furka
"""

# Creating a Tuple

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()


# Tuple with initial values

tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')


# Tuple Length

tpl = ('item1','item2','item3')
len(tpl)

# Accessing Tuple Items

tpl = ('item1','item2','item3')
first_item = tpl[0]

fruits = ('banana','orange','mango','lemon')
second_fruits= fruits[1]

last_index = len(fruits)-1
last_fruit = fruits[last_index]


# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

# Slicing tuples

# Range of Positive Indexes

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

# Range of Negative Indexes

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]


# Changing Tuples to Lists

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0]='apple'
print(fruits)
fruits=tuple(fruits)
print(fruits)


# Checking an Item in a Tuple

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


# Joining Tuples

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# Deleting Tuples

# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits




































