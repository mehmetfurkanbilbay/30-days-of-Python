# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:47:31 2026

@author: furka
"""

# Creating a Dictionary

empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

# Example

person = {
    
    'first name':'john',
    'last name':'doe',
    'age':'25',
    'country':'Spain',
    'is married':False,
    'skills':['C','Python','C++'],
    'address':{
        'street':'Space street',
        'zipcode':'0123456'
        }
    
    }


# Dictionary Length
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
print(len(person)) # 7

# Accessing Dictionary Items
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print(dct['key1'])
print(dct['key4'])



person = {
    
    'first name':'john',
    'last name':'doe',
    'age':'25',
    'country':'Spain',
    'is married':False,
    'skills':['C','Python','C++'],
    'address':{
        'street':'Space street',
        'zipcode':'0123456'
        }
    
    }

print(person['skills'])
print(person['address']['zipcode'])


# Methods

print(person.get('first name'))
print(person.get('address').get('zipcode')) # 0123456
print(person.get('skills')[1]) # Python

# Adding Items to a Dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'


person['job title']='Engineer'
person['skills'].append('Java')
print(person)



# Modifying Items in a Dictionary

dct['key1'] = 'value-one'
print(dct)

person['first name']='Jane'
person['address']['street']='Broadway St'
person['skills'][3]='Machine Learning'


# Checking Keys in a Dictionary

print('street' in person) # False
print('first name'in person) # True



# Removing Key and Value Pairs from a Dictionary

dct.pop('key1') 
dct.popitem() # removes the last item
del dct['key2']



# Changing Dictionary to a List of Items

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None


# Copy a Dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


# Getting Dictionary Keys as a List

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


# Getting Dictionary Values as a List

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])











