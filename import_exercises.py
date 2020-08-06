#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:
# -import the module and refer to the function with the . syntax
# -use from to import the function directly
# -use from and give the function a different name


# In[ ]:


# -import the module and refer to the function with the . syntax
import function_exercises
function_exercises.is_vowel("a")


# In[ ]:


# -use from to import the function directly
from function_exercises import is_two
is_two(2)


# In[ ]:


# -use from and give the function a different name
from function_exercises import get_letter_grade
get_letter_grade(85)


# In[ ]:


# For the following exercises, read about and use the itertools module from the standard library to help
# you solve the problem.
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product

results = [x for x in product('abc', '123')]
print(len(results))


# In[ ]:


# For the following exercises, read about and use the itertools module from the standard library to help
# you solve the problem.
# 2. How many different ways can you combine two of the letters from "abcd"?
import itertools
perm = [x for x in itertools.permutations('abcd', 2)]
print(len(perm))

comb = [x for x in itertools.combinations('abcd', 2)]
print(len(comb))


# In[2]:


# Save this file as profiles.json inside of your exercises directory.
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 


# import json as instructed
import json

# got this from link below to open file and assign is to a variable name
with open('profiles.json') as f:
    data = json.load(f)

# visual to screen to verfiy data
print(data)

# exobrain: https://www.programiz.com/python-programming/json


# In[31]:


# Using this data, write some code that calculates and outputs the following information:
# Total number of users

def total_users(value):
    # create list of id from data
    id_list = [x["_id"] for x in data]
    # return length of list to get # of users
    return(len(id_list))

total_users(data)


# In[ ]:


# Number of active users

# create list of id where active is True
id_list = [x["_id"] for x in data if x['isActive'] == True]
# print length of list to get # of active users
print(len(id_list))


# In[ ]:


# Number of inactive users

# create list of id where active is False
id_list = [x["_id"] for x in data if x['isActive'] == False]
# print length of list to get # of active users
print(len(id_list))


# In[ ]:


# Grand total of balances for all users

def grand_total(value):
    # sum all balances
    balance = [x['balance'] for x in data]
    # strip $ from balance numbers
    rmchar = [x.lstrip("$") for x in balance]
    # remove comma from numbers
    rmcomma = [x.replace(",", "")for x in rmchar]
    # convert numbers to float for addition
    num_bal = [float(x) for x in rmcomma]
    # return sum of all balances
    return(sum(num_bal))

grand_total(data)


# In[ ]:


# Average balance per user

# use grand_total and total_users functions to calculate average balance, rounded for easier reading
avg_bal = grand_total(data) / total_users(data)
# print result to screen to view
print(round(avg_bal, 2))


# In[ ]:


# User with the lowest balance

# get list of all balances
balances = [x["balance"] for x in data]
# find minimum balance in list
min_bal = min(balances)
# print result to screen to view
print(min_bal)


# In[ ]:


# User with the highest balance

# get list of all balances
balances = [x["balance"] for x in data]
# find maximum balance in list
max_bal = max(balances)
# print result to screen to view
print(max_bal)


# In[ ]:


# Most common favorite fruit

# copy function from 101 exercises that counts items and returns total number, adapt to word
def mode(seq):
    max_count = (0, 0)
    for word in seq:
        occur = seq.count(word)
        if occur > max_count[0]:
            max_count = (occur, word)
    return max_count[1]

# get list of all favorite fruits
fav_fruit = [x["favoriteFruit"] for x in data]
# use above function to get most common fruit in list
most_common = mode(fav_fruit)
# print result to screen to view
print(most_common)


# In[ ]:


# Least most common favorite fruit

# copy function above that counts items and returns total number, adapt to least common
def mode_min(seq):
    # need float inf so start at highest when looking for min
    min_count = (float('inf'), float('inf'))
    # count number of times each word in list occurs if occurance count is least set that to min count
    for word in seq:
        occur = seq.count(word)
        if occur < min_count[0]:
            min_count = (occur, word)
    # return the min count position 2 that holds the name of the fruit with the least occurances
    return min_count[1]

# get list of all favorite fruits
fav_fruit = [x["favoriteFruit"] for x in data]
# use above function to get most common fruit in list
least_common = mode_min(fav_fruit)
# print result to screen to view
print(least_common)


# In[47]:


# Total number of unread messages for all users

# find where the number of unread messages in located in the data
# get list of all greetings (where this info is located)
greeting_list = [x["greeting"] for x in data]
# create empty list to store message values later
messages_list = []

# remove . ! and , from greeting
greeting_list = [greeting.replace(".", "") for greeting in greeting_list]
greeting_list = [greeting.replace(",", "") for greeting in greeting_list]
greeting_list = [greeting.replace("!", "") for greeting in greeting_list]
# split list on spaces so # messages will be in same index for all greetings
greeting_list = [greeting.split() for greeting in greeting_list]

# get # of unread messages from string of greeting
for greeting in greeting_list:
    # get correct number and return as integer
    messages = int(greeting[5])
    # append integers to list so can sum
    messages_list.append(messages)

    # print result to screen to view
    print("Total unread messages =", (sum(messages_list)))

# exobrain:
# https://www.geeksforgeeks.org/python-string-split/                
# https://www.kite.com/python/answers/how-to-extract-integers-from-a-string-in-python

