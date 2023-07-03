#!/usr/bin/env python
# coding: utf-8

# In[13]:


# WEEK 1, DAY 2

# BMI CALCULATOR TASK (BODY MASS INDEX)

weight = float(input("Input your weight in kg "))
height = float(input("Input your height in meters "))
height_squared = height **2

result = weight/height_squared
result_str = str(round(result))

print("Your BMI is " + result_str)


# In[10]:


# f-strings task

user_age = input("input your age ")
years_left = 90 - int(user_age)
months_left = years_left*12
weeks_left = years_left*52
Days_left = years_left*365

print(f"You have {Days_left} days, {weeks_left} weeks, and {months_left} months left")


# In[12]:


# BILL TIP CALCULATOR

print("Welcome to the Tip Calculator")
total_bill = input("What is the total bill? $")
tip_percentage = input("What Percentage tip would you like togive? 10, 12, 15? ")
people = input("How many people to split the bill? ")

result = float(total_bill)*(1 + (float(tip_percentage)/100))
final_result = round(result/int(people),2)

print(f"Each person should pay ${final_result}")

