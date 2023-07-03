#!/usr/bin/env python
# coding: utf-8

# In[4]:


# WEEK 1, DAY 3

# IF, ELIF AND ELSE STATEMENTS

# ODD OR EVEN TASK

number = int(input("input any whole number "))

if number%2 == 0:
    print("The Number is Even")
else:
    print("The number is odd")


# In[6]:


num = int(input("input any whole number "))

if num % 2 == 0:
    print("The Number is Even")
   
elif num % 3 == 0:
    print("The number is Prime number")
    
else:
    print("The number is odd")


# In[15]:


# BMI CALCULATOR TASK (BODY MASS INDEX) 2.0

weight = float(input("Input your weight in kg "))
height = float(input("Input your height in meters "))
height_squared = height **2

result = round(weight/height_squared)
result_str = str(result)

print("Your BMI is " + result_str)

if result < 18.5:
    print("You are underweight")
elif result < 25:
    print("You are Normal Weight")
elif result < 30:
    print("You are Overweight")
elif result < 35:
    print("You are Obese")
else:
    print("You are clinically obese")


# In[83]:


# CHECKING FOR LEAP YEAR TASK

year = int(input("Input the year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# In[76]:


# PIZZA EXCERCISE

print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")

elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    print("Check your input and try again")


# In[79]:


# LOVE CALCULATOR

name_1 = input("Type your name here ").lower()
name_2 = input("Type their name here ").lower

# LOVE & TRUE

name_1_L = name_1.count("l")
name_1_O = name_1.count("o")
name_1_V = name_1.count("v")
name_1_E = name_1.count("e")
name_1_T = name_1.count("t")
name_1_R = name_1.count("r")
name_1_U = name_1.count("u")
name_1_ET = name_1.count("e")

name_2_L = name_1.count("l")
name_2_O = name_1.count("o")
name_2_V = name_1.count("v")
name_2_E = name_1.count("e")
name_2_T = name_1.count("t")
name_2_R = name_1.count("r")
name_2_U = name_1.count("u")
name_2_ET = name_1.count("e")

name_1_total = name_1_L + name_1_O + name_1_V + name_1_E + name_1_T + name_1_R + name_1_U + name_1_ET
name_2_total = name_2_L + name_2_O + name_2_V + name_2_E + name_2_T + name_2_R + name_2_U + name_2_ET

score = str(name_1_total) + str(name_2_total)
new_score = int(score)

if new_score < 10 or new_score > 90:
    print(f"Your score is {new_score}, you go together like coke and mentos")
elif new_score >= 40 and new_score <= 50:
    print(f"Your score is {new_score}, you are alright together")
else:
    print(f"Your score is {new_score}")


# In[90]:


# ADVENTURE GAME TASK

print("Welcome to the Adventure Ridge, start your journey to win an iphone 14 pro max...")

c1 = input("Which way would you like to go, Left or Right? L or R ")
if c1 == "R":
    c2 = input("Which door would you like to open, Red, Blue or Yellow? R or B or Y ")
    if c2 == "B":
        c3 = input("Which box would you like to open, White or Black? W or B ")
        if c3 == "B":
            c4 = input("Use your key to open one safebox, Gold, Silver or Diamond? G or S or D ")
            if c4 == "D":
                print("Congratulations! You win an iphone 14 pro max")
            else:
                print("Sorry, the safebox contained cobwebs only! Game Over!")
        else:
            print("The Box is Empty! Game Over!")
    else:
        print("The room is empty! Game Over!")
else:
    print("Road Blocked! Game Over!")

