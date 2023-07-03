#!/usr/bin/env python
# coding: utf-8

# In[17]:


# WEEK 2, DAY 9

# DICTIONARIES AND NESTING

student_scores = {"Harry": 81,
                  "Ron": 78,
                  "Hermione": 99,
                  "Draco": 74,
                  "Neville": 62,
}

student_grades = {}

for student_score in student_scores:
    score = student_scores[student_score]
    if score > 90 and score < 101:
        student_grades[student_score] = "Outstanding"
    elif score > 80 and score < 91:
        student_grades[student_score] = "Exceeds Expectations"
    elif score > 70 and score < 81:
        student_grades[student_score] = "Acceptable"
    elif score < 71:
        student_grades[student_score] = "Fail"
    
    
print(student_grades)


# In[3]:


# NESTING

travel_log = [
{
    "Country": "France", 
    "Visits": 12, 
    "Cities":["paris", "Lille", "Dijon"],
},
{
    "Country": "Germany", 
    "Visits": 5, 
    "Cities":["Berlin", "Hamburg", "Stuttgart"],
},
]


def add_new_country(country, visits, cities):
    new_dic = {"Country": country, "Visits": visits, "Cities": cities}
    travel_log.append(new_dic)

    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# In[49]:


# SECRET BID PROJECT

print("Welcome to the Secret Bid Programme!")

bid_dic = {}

other = True

highest = 0

while other:
    name_of_bidder = input("What is your name? ")
    price_of_bidder = int(input("What is your Bid Price? $"))

    bid_dic[name_of_bidder] = price_of_bidder
    
    ask = input("Is there any other bidder? Type 'yes' or 'no': ").lower()

    if ask == "no":
        other = False
        for bidder in bid_dic:
            if bid_dic[bidder] > highest:
                winner = bidder
                highest = bid_dic[bidder]
        print(f"The highest bidder is {winner} with a bid of ${highest}!")


# In[ ]:





# In[ ]:




