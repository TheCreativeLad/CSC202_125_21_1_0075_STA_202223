#!/usr/bin/env python
# coding: utf-8

# In[10]:


#### HANGMAN GAME PROJECT

logo = ['''

 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _' | '_ \ / _' | '_ ` _ \ / _' | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| | |\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/

''']

print(logo)

print("Welcome to Hangman Game!")

word_list = ["secure", "mouse", "statistics", "book", "project", "Welcome", "awkward", "checkpoint", "beautiful", "widgets",
            "minutes", "school", "avenue", "bliss", "syndicate", "reaction", "mimick", "handsome", "photosynthesis", "theory",
            "thesis", "project", "frame", "understanding", "backward", "october", "shepherd", "control", "disguise", "franchise",
            "bookmark", "bootstrap", "collaborate", "documentation", "philosophy", "chromatography", "qualify", "zeal", "oxen",
            "exercise"]

import random

stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
---------
---------
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
---------
---------
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
---------
---------
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
---------
---------
''','''
 +---+
 |   |
 O   |
/    |
     |
     |
---------
---------
''','''
 +---+
 |   |
 O   |
     |
     |
     |
---------
---------
''','''
 +---+
 |   |
     |
     |
     |
     |
---------
---------
''']

chosen_word = random.choice(word_list)

lives = 6

display = []
for char in range(len(chosen_word)):
    display += "_"
    

print(display)

missing = "_"
lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for c in range(len(chosen_word)):
        if chosen_word[c] == guess:
            display[c] = guess
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guess letter {guess}, that's not in the word, you lose a life!")
        if lives == 0:
            end_of_game = True
            print("You lose")
            
    print(f"{' '.join(display)}")
            
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])

