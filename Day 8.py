#!/usr/bin/env python
# coding: utf-8

# In[18]:


# WEEK 2, DAY 8

# def greet():
#     print("Hello!")
#     print("Good")
#     print("Morning")
    
# greet()


# name = input("Type your name:\n")
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"Good morning {name}")
#     print("How ar you doing today?")
    
# greet_with_name(f"{name}")


names = input("What is your name?\n")
location = input("Where are you from?\n")

def greet_with(names, location):
    print(f"Hello {names}!")
    print(f"Wow! you are from {location}")
    
greet_with(f"{names}", f"{location}")


# In[29]:


# AREA CALCULATION EXERCISE

import math

def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil((height*width)/coverage)} cans of paints.")


test_h = int(input("Height of wall? "))
test_w = int(input("Width of wall? "))
coverage = 5

paint_calc(height = test_h,  width = test_w, cover = coverage)


# In[62]:


# PRIME NUMBER CHECKER

def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number = n)


# In[29]:


# CAESAR CIPHER PROJECT

def project():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", 
                "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", 
                "v", "w", "x", "y", "z"]

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(message, shift_number, direct):
        if shift_number > 25:
            shift_number %= 25
            print("shift number cannot be greater than 10! the program will use 25 as shift number")
        
        coded_text = ""
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                if direct == "encode":
                    new_position = position + shift_number
                    new_letter = alphabet[new_position]
                    coded_text += new_letter

                if direct == "decode":
                    new_position = position - shift_number
                    new_letter = alphabet[new_position]
                    coded_text += new_letter
            else:
                coded_text += char
                
        print(f"The {direct}d text is: {coded_text}")


    caesar(message = text, shift_number = shift, direct = direction)
    
    
    question = input("Would you like to run this program again? type yes or no\n").lower()
    if question == "yes":
        project()
    elif question == "no":
        print("Goodbye!")
    else:
        print("Your decision is not specific, Goodbye!")
    
    
project()


# In[ ]:




