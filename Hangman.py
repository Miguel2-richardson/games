# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:32:19 2021

@author: Miguel
"""

from random import randint as rand

global word_bank 
word_bank = ["Fellow", "Hello", "Chess"]
global guessed
guessed = []
global word
global game_word
global wrong_cnt
wrong_cnt = 0

#Uses guess and holder to put letters in postion for the game
def build_word(holder, guess):
    global game_word
    for i in holder:
        game_word[i] = guess
    return(game_word)

#Builds man for incorrect answer
def build_man():
    global wrong_cnt
    if wrong_cnt == 0:
        print("_|_")
        return(0)
    if wrong_cnt == 1:
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 2:
        print(" | ")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 3:
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 4:
        print(" __")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 5:
        print(" ___")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 6:
        print(" ___")
        print(" |  |")
        print(" | ")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 7:
        print(" ___")
        print(" |  |")
        print(" |  O")
        print(" | ")
        print("_|_")
        return(0)
    if wrong_cnt == 7:
        print(" ___")
        print(" |  |")
        print(" |  O")
        print(" | /|\\")
        print("_|_")
        return(0)
    if wrong_cnt == 8:
        print(" ___")
        print(" |  |")
        print(" |  O")
        print(" | /|\\")
        print("_|_/ \\")
        return(0)
    return(0)

#Finds letter match and postion
def compare(guess):
    global wrong_cnt
    count = 0
    index = 0
    holder = [] #contains index postions of matched characters
    for i in word:
        if i == guess:
            count +=1
            holder.append(index)
        index += 1    
    if count == 0:
        print(guess, " not found")
        wrong_cnt += 1
    else:
        print(guess, "found")
    return(holder)

# Handles display in console
def display():
    lines = len(word)
    print("_ "*lines)
    print(guessed)
    return(0)

#Takes in user input and checks that it is of length 1.
def read():
    guess = input("Guess 1 letter: ").lower()#enforces lowercase for comparison
    if len(guess) == 1 and guess not in guessed:
        guessed.append(guess)
    else:
        print("That wasn't 1 letter, or was already guessed. Try again: ")
        guess = read()
    return(guess)

#Randomly selects a word from word_bank
def select():
    choice = 0#rand(0,(len(word_bank) - 1))
    choice = word_bank[choice].lower() #lowercase f is different from uppercase F, removes having to worry about this
    return(choice)



    


print("Hangman. ")
word = select()
game_word = ["_"]*len(word)
# display()
#read()
# display()
#check = read()

guess = read()
holder = compare(guess)
test = build_word(holder, guess)
wrong_cnt = 5
build_man()

#Make a file for functions, and call that library.
#Need to add a loop to facilitate the game. 
#Termination condition can be from return value of build_man.
#When wrong_cnt == 8 game ends. 
