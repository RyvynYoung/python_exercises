#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Conditional Basic a. prompt the user for a day of the week, print out whether the day is Monday or not

day = input('What day is it? ')
day = day.lower()
if day == 'monday':
    print('Today is Monday')
else:
    print('not Monday')


# In[ ]:


# 1. b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = input('What day is it? ')
day = day.lower()
if day == 'saturday' or day == 'sunday':
    print("It's the weekend!!")
else:
    print('Today is a weekday')


# In[ ]:


# 1. c. create variables and make up values for: the number of hours worked in one week, the hourly rate, 
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours

hours = 41
OT_hours = 0
rate = 10
OT_rate = rate * 1.5
weekly_pay = 0

if hours >= 40:
    OT_hours = hours - 40
    hours = 40
    
weekly_pay = "${:,.2f}".format(hours * rate + OT_hours * OT_rate)
print(weekly_pay)


# In[ ]:


# 2. Loop Basics a. While
# - Create an integer variable i with a value of 5.
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one.
# - Your output should look like this:
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

i = 5
while i <= 15:
    print(i)
    i += 1


# In[ ]:


# 2. a. Create a while loop that will count by 2's starting with 0 and ending at 100. 
i = 2
while i <= 100:
    print(i)
    i += 2


# In[ ]:


# 2. a. Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5


# In[ ]:


# 2. a. Ceate a while loop that starts at 2, and displays the number squared on each line while the 
# number is less than 1,000,000. Output should equal:
#  2
#  4
#  16
#  256
#  65536

i = 2
while i < 100000:
    print(i)
    i = i ** 2


# In[ ]:


# 2. a. Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

i = 100
while i >= 5:
    print(i)
    i -= 5


# In[ ]:


# 2. b. For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for 
# that number.

# For example, if the user enters 7, your program should output:


# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

num = int(input('Enter a whole number: '))
i = 1
for i in range(11):
    print(num, 'x', i, '=', num * i)

    


# In[ ]:


# 2.b.ii. Create a for loop that uses print to create the output shown below.


# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

i = 1
for i in range(10):
    print(str(i) * i)
    i += 1


# In[ ]:


# 2.c. break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting
# the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

# Your output should look like this:


# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

get_num = False
while get_num == False:
    num = input("Enter an odd number between 0 and 50: ")
    if num.isdigit():
        num = int(num)
        if num > 0 and num <50 and num % 2 == 1:
            break
        else:
            print("That is not an odd number between 0 and 50")
    else:
        print("That is not a valid number")
        
print("The number to skip is:", num)
i = 1
for i in range(50):
    if i == num:
        print("Yikes, skipping this number", num)
        continue
    elif i % 2 == 1:
        print("Here is an odd numer:", i)


# In[ ]:


# 2.d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

get_num = False
while get_num == False:
    num = input("Enter a postive number: ")
    if num.isdigit():
        num = int(num)
        if num > 0:
            break
    else:
        print("That is not a valid number")
        
print("The number to to count to is:", num)
i = 0
for i in range(num + 1):
    print(i)
    i += 1


# In[ ]:


# 2.e. Write a program that prompts the user for a positive integer. Next write a loop that prints
# out the numbers from the number the user entered down to 1.

get_num = False
while get_num == False:
    num = input("Enter a postive number: ")
    if num.isdigit():
        num = int(num)
        if num > 0:
            break
    else:
        print("That is not a valid number")
        
print("The number to to count down from is:", num)
i = num
while i > 0:
    print(i)
    i -= 1
    
    # for loop return in ascending order, while loop will return descending


# In[ ]:


# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

i = 1
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
        
        # have to look for muiltiples of both first otherwise none will be FizzBuzz because stops looking once earlier condition is met
        


# In[1]:


# 4. Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

contin = "y"
while contin == "y":
    num = int(input("Enter an integer you would like to go up to: "))
    for i in range(1, num + 1):
        print("Number:", i, "Squared:", i ** 2, "Cubed:", i ** 3)
    contin = input("Would you like to continue? enter y for yes or n for no: ")


# In[2]:


##### Bonus: Research python's format string specifiers to align the table


contin = "y"
while contin == "y":
    num = int(input("Enter an integer you would like to go up to: "))
    row = "| {number:10d} | {squared:10d} | {cubed:10d} |".format
    for i in range(1, num + 1):
    
        print(row(number = i, squared = i ** 2, cubed = i ** 3))
    contin = input("Would you like to continue? enter y for yes or n for no: ")




    # exobrain resources:
    # https://mkaz.blog/code/python-string-format-cookbook/


# In[ ]:


# 5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0


contin = "y"
while contin == "y":
    num = int(input("Enter a numerical grade from 0 - 100: "))
    if 100 >= num >= 88:
        print("A")
    elif 87 >= num >= 80:
        print("B")
    elif 79 >= num >= 67:
        print("C")
    elif 66 >= num >= 60:
        print("D")
    elif 59 >= num >= 0:
        print("F")
    else:
        print("not valid input")
    contin = input("Would you like to continue? enter y for yes or n for no: ")
    


# In[ ]:


# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).


contin = "y"
while contin == "y":
    num = int(input("Enter a numerical grade from 0 - 100: "))
    if 100 >= num >= 88:
        if 100 >= num >= 99:
            print("A+")
        elif 89 >= num >= 88:
            print("A-")
        else:
            print("A")
    if 87 >= num >= 80:
        if 87 >= num >= 86:
            print("B+")
        elif 81 >= num >= 80:
            print("B-")
        else:
            print("B")
    if 79 >= num >= 67:
        if 79 >= num >= 78:
            print("C+")
        elif 68 >= num >= 67:
            print("C-")
        else:
            print("C")
    if 66 >= num >= 60:
        if 66 >= num >= 65:
            print("D+")
        elif 61 >= num >= 60:
            print("D-")
        else:
            print("D")
    if num <= 59:
        print("F")
    contin = input("Would you like to continue? enter y for yes or n for no: ")
    


# In[ ]:


# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

keys = ['title', 'author', 'genre']

book1 = ['Nuture by Nature', 'Tieger', 'parenting']
book2 = ['Raising Your Spirited Child', 'Kurcinka', 'parenting']
book3 = ['blink', 'Gladwell', 'business']
book4 = ['Outliers', 'Gladwell', 'business']
book5 = ['The Explosive Child', 'Greene', 'parenting']
book6 = ['Raising Human Beimgs', 'Greene', 'parenting']
book7 = ['Coding Porjects in Python', 'Vorderman', 'python']
book8 = ['Coding Games in Python', 'Vorderman', 'python']
book9 = ['Coding Porjects in Python', 'Vorerman', 'python']
book10 = ['The Warior Heir', 'Chima', 'fiction']
book11 = ['The Demon King', 'Chima', 'fiction']
book12 = ['World War Z', 'Brooks', 'fiction']
book13 = ['Off Armagedon Reef', 'Weber', 'fiction']

dict_list = []
dict_list.append(dict(zip(keys, book1)))
dict_list.append(dict(zip(keys, book2)))
dict_list.append(dict(zip(keys, book3)))
dict_list.append(dict(zip(keys, book4)))
dict_list.append(dict(zip(keys, book5)))
dict_list.append(dict(zip(keys, book6)))
dict_list.append(dict(zip(keys, book7)))
dict_list.append(dict(zip(keys, book8)))
dict_list.append(dict(zip(keys, book9)))
dict_list.append(dict(zip(keys, book10)))
dict_list.append(dict(zip(keys, book11)))
dict_list.append(dict(zip(keys, book12)))
dict_list.append(dict(zip(keys, book13)))

for item in dict_list:
    print(', '.join([item[key] for key in keys]))
    

    # exobrain sources:
    # https://bytes.com/topic/python/answers/781432-how-create-list-dictionaries
    # https://realpython.com/python-zip-function/
    


# In[ ]:


# 6.a.Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books
# in that genre.

requested = input("What genre would you like titles for? ")
for item in dict_list:
    if item['genre'] == requested:
        print(item['title'])
        


# In[ ]:




