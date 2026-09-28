# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:33:23 2026

@author: furka
"""

# Creating a set

#syntax
st=set()

# Creating a set with initial items
st = {'item1','item2','item3','item4'} 


# Getting Set's Length
st = {'item1','item2','item3','item4'}
len(st)

# Accessing items in a set

st = {'item1','item2','item3','item4'}
print('Does set st contain item3?', 'item3' in st)


# Adding items to a Set

st = {'item1','item2','item3','item4'}
st.add('item5')

# Add multiple items

st = {'item1','item2','item3','item4'}
st.update(['item5','item6','item7'])


fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)


# Removing items from a set

st = {'item1','item2','item3','item4'}
st.remove('item1')


# The pop() methods remove a random item from a list and it returns the removed item.

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

# Clearing Items in a Set

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# Deleting a Set

st = {'item1', 'item2', 'item3', 'item4'}
del st

# Converting List to Set

lst =['item1','item2','item3','item4','item1']
st = set(lst) #  - the order is random, because sets in general are unordered

# Joining Sets

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

# Finding Intersection Items

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2


python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon

# Checking Subset and Super Set

"""
Subset: issubset()
Super set: issuperset
"""

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# Example

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False


# Checking the Difference Between Two Sets

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1


# Finding Symmetric Difference Between Two Sets

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1


# Joining Sets

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}






