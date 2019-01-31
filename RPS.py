# -*- coding: utf-8 -*-


# Import GUI Library and random Library
from tkinter import *
from tkinter import ttk
import random

#Lists for randomized messages used in outcomes
options = ("ROCK", "PAPER", "SCISSORS")
Wins = ("You're no match for machines.", "I win, computers read minds.",\
        "Better luck next time, sucker.")
Losses = ("You win, Seth didn't program me right.", "What? How'd you win?",\
          "I lost because I was reading your email.")
Ties = ("Tie, just trying to help your self esteem.", "Ties are just as bad as losing.",\
        "My, my, my, we got a tie. My tie.")
Rock = ("Rock! You Ready!?", "Let's Rock and Roll!", "Rock! Okay!")
Paper = ("Paper? Let's go lightweight", "Paper!? Let's do it!", "Paper. You're done!")
Scissors = ("Scissors! Let's cut to it!", "Scissors, alrighty then!", "Scissors are for sissies!")

#Event triggered when Rock is clicked
def RockF(event):
    RkChoice = random.choice(Rock)
    CompCh.delete(0, "end")
    MainScreen.delete(0, "end")
    MainScreen.insert(0, RkChoice)
    PlayerCh.delete(0, "end")
    PlayerCh.insert(0, "ROCK")
    
#Event triggered when Paper is clicked
def PaperF(event):
    PprChoice = random.choice(Paper)
    CompCh.delete(0, "end")
    MainScreen.delete(0, "end")
    MainScreen.insert(0, PprChoice)
    PlayerCh.delete(0, "end")
    PlayerCh.insert(0, "PAPER")
    
    
#Event triggered when scissors is clicked
def ScissorsF(event):
    ScsrChoice = random.choice(Scissors)
    CompCh.delete(0, "end")
    MainScreen.delete(0, "end")
    MainScreen.insert(0, ScsrChoice)
    PlayerCh.delete(0, "end")
    PlayerCh.insert(0, "SCISSORS")
    
    
# Event triggered when Fight is clicked
def FightF(event):
    PlChoice = PlayerCh.get()   
    CmpChoice = random.choice(options)
    CompCh.delete(0, "end")
    CompCh.insert(0, CmpChoice)
    if PlChoice == CmpChoice:
        TieMsg = random.choice(Ties)
        MainScreen.delete(0, "end")
        MainScreen.insert(0, TieMsg)
    elif PlChoice == "ROCK" and CmpChoice == "PAPER" or PlChoice == "PAPER"\
    and CmpChoice == "SCISSORS" or PlChoice == "SCISSORS" and CmpChoice ==\
    "ROCK":
        WinMsg = random.choice(Wins)
        MainScreen.delete(0, "end")
        MainScreen.insert(0, WinMsg)
    else:
        LossMsg = random.choice(Losses)
        MainScreen.delete(0, "end")
        MainScreen.insert(0, LossMsg)

#Code for the GUI interface
root = Tk()

Label(root, text="     ").grid(row=0, column=0)
Label(root, text="     ").grid(row=1, column=0)
Label(root, text="     ").grid(row=1, column=6)
Label(root, text="It's time for...").grid(row=1, column=3)
Label(root, text="Rock! Paper! Scissors!").grid(row=2, column=3)
Label(root, text="     ").grid(row=3, column=1)
MainScreen = Entry(root, width=50)
MainScreen.grid(row=4, column=3)
MainScreen.insert(0, "Choose your weapon!")
Label(root, text="     ").grid(row=5, column=3)

RockButton = Button(root, text="ROCK")
RockButton.grid(row=6, column=1)
RockButton.bind("<Button-1>", RockF)


PaperButton = Button(root, text="PAPER")
PaperButton.grid(row=6, column=3)
PaperButton.bind("<Button-1>", PaperF)

ScissorsButton = Button(root, text="SCISSORS")
ScissorsButton.grid(row=6, column=5)
ScissorsButton.bind("<Button-1>", ScissorsF)

Label(root, text="     ").grid(row=7, column=0)

FightButton = Button(root, text="Fight!")
FightButton.grid(row=8, column=3)
FightButton.bind("<Button-1>", FightF)

Label(root, text="     ").grid(row=9, column=0)

PlayerCh = Entry(root)
PlayerCh.grid(row=10, column=1)
PlayerCh.insert(0,"")

Label(root, text="Versus").grid(row=10, column=3)

CompCh = Entry(root)
CompCh.grid(row=10, column=5)
CompCh.insert(0,"")

Label(root, text="     ").grid(row=11, column=0)


root.mainloop() 
