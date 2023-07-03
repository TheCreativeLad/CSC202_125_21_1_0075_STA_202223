#!/usr/bin/env python
# coding: utf-8

# In[93]:


import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(round(random_float * 5, 1))


# In[146]:


love_score = random.randint(1,100)

if love_score < 20 or love_score >= 50 and love_score <= 70:
    print(f"Your love score is {love_score}, You are not compatible with each other")
else:
    print(f"Your love score is {love_score}, You are Compatible with each other")


# In[158]:


import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_number = random.randint(0, 1)

if random_number == 0:
    print("Head")
else:
    print("Tail")


# In[193]:


import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

name_input = input("Typet everybody's names separated by a comma and a space: ")
names = name_input.split(", ")
name0 = names[0]
name1 = names[1]
name2 = names[2]
name0 = names[3]
name1 = names[4]

x = len(names)
random_number = random.randint(0, x-1)

payee = names[random_number]

print(f"{payee} is going to buy the meal today!")


# In[196]:


import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

name_input = input("Typet everybody's names separated by a comma and a space: ")
names = name_input.split(", ")

payee = random.choice(names)

print(f"{payee} is going to buy the meal today!")


# In[22]:


# TREASURE MAP CHALLENGE

print("Welcome to the Treasure Map!")

row1 = ["⚫","⚫","⚫"]
row2 = ["⚫","⚫","⚫"]
row3 = ["⚫","⚫","⚫"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put your treasure? column then row format: ")
column = int(position[0])
row = int(position[1])

map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# In[7]:


# ROCK, PAPER AND SCISSORS GAME

import random

print("Welcome to Rock, Paper, Scissors Game!")

rock = "👊"
paper = "📰"
scissors = "✂"

Board = [rock, paper, scissors]

user_input = input("0 for rock, 1 for paper, 2 for scissors: ")
user_choice = Board[int(user_input)]
computer_choice = random.choice(Board)

print(f"Your choice\n{user_choice}\n\nComputer choice\n{computer_choice}")

if user_choice == computer_choice:
    print("It is a Draw!")
elif user_choice == rock and computer_choice == scissors:
    print("You Win!")
elif user_choice == scissors and computer_choice == paper:
    
    print("You Win!")
elif user_choice == paper and computer_choice == rock:
    print("You Win!")
else:
    print("You Lose!")


# In[ ]:




