#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a file named function_exercises.py for this exercise. After creating each function specified below, 
# write the necessary code in order to test your function.


# In[59]:


# 1. Define a function named is_two. It should accept one input and return True if the passed
# input is either the number or the string 2, False otherwise.

def is_two(n):
    # as these are the only 2 acceptable values no other assertions are needed, any other value should return false
    return n == 2 or n == '2'

# assertion statements to test function
assert is_two(2) == True
assert is_two('2') == True
assert is_two(4) == False
assert is_two('five') == False
assert type(is_two(2)) == bool #added during demo, but it passed without needing changes to function

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[56]:


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(v):
    assert len(v) == 1, "please input a single letter only" # verifies input is single letter only
    
    vowel = ['a', 'e', 'i', 'o', 'u'] # list of vowels for comparison
    
# ensures input is in lower case then checks if input is in list above and returns true if in list, false if not in list
    return v.lower() in vowel 
    
# assertion statements to test function
assert is_vowel('a') == True
assert is_vowel('b') == False
assert is_vowel('A') == True
assert is_vowel('f') == False
assert type(is_vowel('a')) == bool #added during demo, but it passed without needing changes to function

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[61]:


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(c):
    # if is_vowel is false this is a consonant
    return is_vowel(c) == False

# assertion statements to test function
assert is_consonant('a') == False
assert is_consonant('b') == True
assert is_consonant('D') == True
assert is_consonant('I') == False
assert type(is_two(2)) == bool #added during demo, but it passed without needing changes to function

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[39]:


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.

def capitalize_word_if_consonant(w):
    
    # check if the first letter of the word is a consonant using is_consonant function
    if is_consonant(w[0]) == True:
        # if it is then capitalize the word
        return w.capitalize()
    else:
        #if not return the word without change
        return w

# assertion statements to test function
assert capitalize_word_if_consonant('hello') == 'Hello'
assert capitalize_word_if_consonant('every') == 'every'
assert capitalize_word_if_consonant('awesome') == 'awesome'
assert capitalize_word_if_consonant('rest') == 'Rest'

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[30]:


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(t, b):
    # assertion to verify input is either an in integer or float
    assert type(b) == int or type(p) == float, "Invalid Input"
    # assertion to verify input is a float
    assert type(t) == float, "Invalid Input"
    # return tip value rounded to 2 decimal places
    return round((t * b), 2)

# assertion statements to test function
assert calculate_tip(.1, 10) == 1.00
assert calculate_tip(.25, 100) == 25.00

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[29]:


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(p, d):
    # assertion to verify input is either an in integer or float
    assert type(p) == int or type(p) == float, "Invalid Input"
    # assertion to verify input is a float
    assert type(d) == float, "Invalid Input"
    # calculate price after discount
    disc_price = p - p * d
    # return discounted price rounded to 2 decimal places
    return round(disc_price, 2)

# assertion statements to test function
assert apply_discount(100, .1) == 90.00
assert apply_discount(150, .25) == 112.50

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[28]:


# 7. Define a function named handle_commas.
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(num):
    # assertion to verfiy number is a string
    assert type(num) == str, "invalid input"
    # remove the comma
    num = num.replace(",", "")    
    # convert the number to a float, allows for decimals
    num = float(num)
    # return the number
    return(num)

# assertion statements to test function
assert handle_commas('100,000') == 100_000
assert handle_commas('1,000.75') == 1_000.75

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[27]:


# 8. Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num):
    # assertion to verify input is an integer
    assert type(num) == int, "invalid input"
    # if statements to find letter grade, only need minimum score because higher numbers will have already
    # been assigned a letter
    if num >= 88:
        return("A")
    elif num >= 80:
        return("B")
    elif num >= 67:
        return("C")
    elif num >= 60:
        return("D")
    else:
        return("F")

# assertion statements to test function       
assert get_letter_grade(92) == 'A'
assert get_letter_grade(85) == 'B'
assert get_letter_grade(68) == 'C'
assert get_letter_grade(62) == 'D'
assert get_letter_grade(43) == 'F'

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[26]:


# 9.Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# copied directly from 101 exercises to save time
def remove_vowels(value):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in value:
        if i in vowel:
            value = value.replace(i, "")
    return(value)

# assertion statements to test function   
assert remove_vowels("banana") == "bnn"
assert remove_vowels("ubuntu") == "bnt"
assert remove_vowels("mango") == "mng"
assert remove_vowels("QQQQ") == "QQQQ"

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[1]:


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed 
# leading and trailing whitespace should be removed =.strip
# everything should be lowercase =.lower
# spaces should be replaced with underscores = .replace
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


# see also notes below

# modified removed vowels function to remove special characters instead
def remove_spec_char(value):
    spec_char = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-'] #list of characters to remove
    # loop to check each character to see if it is a special character and remove as needed
    for i in value:
        if i in spec_char:
            value = value.replace(i, "")
    return(value)  # returns value for use in next function

def normalize_name(value):
    # verify input type is a string
    assert type(value) == str
    # change the string to lowercase
    norm_name = value.lower()
    # remove special characters using above function
    norm_name = remove_spec_char(norm_name)
    # remove leading and trailing white space
    norm_name = norm_name.strip()
    # replace spaces with underscore
    norm_name = norm_name.replace(" ", "_")
    # return normalized name
    return norm_name

# assertion statements to test function 
assert normalize_name("Name") == "name"
assert normalize_name("First Name") == "first_name"
assert normalize_name("% completed") == "completed"
assert normalize_name("    $   Ryvyn Young    ") == "ryvyn_young"

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# still stuck at time of review, not answered
# got it working by copying my remove vowels function from 101 exercises and modifying list of characters
# then used that function to remove special characters listed, but list is not all inclusive


# In[78]:


# verfiy end result of normalize name above passes the isidentifier test

normalize_name("    $   Ryvyn Young    ").isidentifier()


# In[59]:


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is 
# the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# completed before walk through

def cumulative_sum(x):
    sum_list = [] # set up an empty list for added values
    y = 0   # set up an empty varible to hold sum
    # for each number in the input list add value y is holding then add it to the sum_list
    for n in x:
        y = y + n
        sum_list.append(y)
    # return list of summed values
    return sum_list

# assertion statements to test function 
assert cumulative_sum([1, 1, 1]) == [1, 2, 3]
assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert cumulative_sum([]) == [] # added during walk throu
# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[58]:





# In[32]:


# Bonus
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return 
# a string that is the representation of the time in a 24-hour format. 

#completed before walk through 

def twelveto24(time):
    # checks to see if input is am by looking for letter a in string, removes am if found
    if "a" in time:
        time = time.rstrip("am")
    # checks to see if input is pm by looking for letter p in string,
    elif "p" in time:
        # remove pm
        time = time.rstrip("pm")
        # convert : to . so that can convert to float in next step
        time = time.replace(":", ".")
        # convert to float so that can add 12 in next step, can't add integer 12 to string
        time = float(time)
        # add 12 hours to convert pm time to 24 hour
        time = time + 12
        # convert back to string for display purposes
        time = str(time)
        # convert . to : for display purposes
        time = time.replace(".", ":")
    # handle time not input with am or pm
    else:
        print("please enter time with am or pm")
    # return time
    return time

# assertion statements to test function 
assert twelveto24("4:40am") == "4:40"
assert twelveto24("10:45am") == "10:45"
assert twelveto24("4:45pm") == "16:45"
assert twelveto24("10:45pm") == "22:45"
assert twelveto24("10:00") == "10:00"

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[60]:


# Bonus write a function that does the opposite.

# completed before walk through

def twentyfourto12(time):
    # check input is a string
    assert type(time) == str, "please enter time as HH:MM"
    # would like to put assertions here to check 1st 2 digits are digits and last 2 are digits using isdigit?
    # replace the : with . to allow for conversion to float in next step 
    time = time.replace(":", ".")
    # convert to float to allow for substrating
    time = float(time)
    # check to see if the time is less than 13:00, those will all be am times
    if time < 13.00:
        # convert input back to string for formating
        time = str(time)
        # replace : with .
        time = time.replace(".", ":")
        # add am to end
        time = time + "am"
    # pm times need to have 12 hours subtracted
    elif time >= 13.00:
        # subtract 12 hours
        time = time - 12
        # round to 2 decimals before converting back to string
        time = round(time, 2)
        # convert to string for display formating
        time = str(time)
        # replace . with : for display
        time = time.replace(".", ":")
        # add pm to end for display
        time = time + "pm"
    # handle inputs that have am or pm
    else:
        print("please enter time as HH:MM")
    # return time
    return time

# NOTE: this does not handle minutes ending in 0 ie. 4:40 will be 4:4am
# alternative solution presented in demo using index position of digits would work better

# assertion statements to test function
assert twentyfourto12("4:45") == "4:45am"
assert twentyfourto12("10:45") == "10:45am"
assert twentyfourto12("16:42") == "4:42pm"
assert twentyfourto12("22:45") == "10:45pm"

# visual confirmation to screen that all tests passed
print("Passes all assertions")


# In[ ]:


# Bonus
# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the 
# index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# I have no idea where to start other than goggle. If time allows I'll return to this.
# instead available time will first be used to annotate completed questions as required
# reference Adam's presentaton/code for help

