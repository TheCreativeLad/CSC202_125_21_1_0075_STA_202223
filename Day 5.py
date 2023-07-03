#!/usr/bin/env python
# coding: utf-8

# In[21]:


# DAY 5

# HEIGHT AVERAGE EXCERCISE

students_height = input("Type the students height separated by space ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

average_height = sum(students_height)/len(students_height)
print(average_height)
print(round(average_height))


# In[28]:


students_height = input("Type the students height separated by space ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

length_height = 0
total_height = 0
for num in students_height:
    total_height += num
    length_height += 1
print(round(total_height/length_height))
# print(length_height)


# In[11]:


# FINDING THE HIGHEST VALUE

students_scores = input("Type the students height separated by space ").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)

highest = 0
for i in students_scores:
    if i > highest:
        highest = i
print(f"The highest score is: {highest}")


# In[16]:


# FOR LOOPS WITH RANGE FUNCTION

sum = 0
for numbers in range(0,101):
    sum += numbers
print(sum)


# In[19]:


# SUM OF ALL EVEN NUMBERS IN 1 - 100

sum_even =  0
for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number
print(sum_even)


# In[23]:


# FIZZBUZZ EXCERSICE

for game in range(1, 101):
    if game % 3 == 0 and game % 5 == 0:
        game = "FizzBuzz"
    elif game % 3 == 0:
        game = "Fizz"
    elif game % 5 == 0:
        game = "Buzz"
    print(game)


# In[44]:


# PyPassword Generator Project

import random 

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "@", "#", "$", "%", "&", "*",  "(", ")", "+", "?"]

print("Welcome to PyPassword Generator!")

nr_letters = int(input("How many letters would you love your password to have?\n"))
nr_numbers = int(input("How many numbers would you love your password to have?\n"))
nr_symbols = int(input("How many symbols would you love your password to have?\n"))

password = []

for p in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters
    
for w in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers
    
for q in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols
    
random.shuffle(password)

new_password = ""
for char in password:
    new_password += char
print(f"Your password is {new_password}")

