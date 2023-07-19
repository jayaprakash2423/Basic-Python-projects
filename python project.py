#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python project 1
# simple calculator

from tkinter import*

me=Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATOR",bg='dark gray',font=("Times",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
metext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue')
metext.pack()

but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(me,padx=14,pady=14,bd=4,bg='white',text="",command=lambda:clickbut(""),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(me,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
me.mainloop()


# In[2]:


# python project 2
# the simple age calculator
from datetime import date
today = date.today()
 
def exit():
    window.destroy()
def get_age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')
 
l1 = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")
 
l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)
e3=tk.Entry(window,width=5)
 
b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=get_age)
 
l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
t1=tk.Text(window,width=5,height=0,state="disabled")
 
b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)
 
l1.place(x=70,y=5)
l2.place(x=10,y=40)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=240,y=203)
b2.place(x=100,y=230)
window.mainloop()


# In[3]:


# python project 3
#  tic-tac-toe game

import random
# Initializing the number of places in a board
board_values=[i for i in range(0,9)]
# Initializing both players to null character
You, computer = '',''

# Making tuples pairs as corners,center and other places
moves=((1,7,3,9),(5,),(2,4,6,8))
# Initalizing all the winning Combinations
win_comb=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

table=range(1,10)

def print_board():
    x=1
    for i in board_values:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='----------\n';
        char=' '
        if i in ('X','O'): 
            char=i
        x+=1
        print(char,end=end)
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, You, move):
    if move in table and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, You, move):
    places=[]
    x=0
    for i in brd:
        if i == You: 
            places.append(x);
        x+=1
    win=True
    for vi in win_comb:
        win=True
        for h in vi:
            if brd[h] != You:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, You, move, undo=False):
    if can_move(brd, You, move):
        brd[move-1] = You
        win=can_win(brd, You, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# AI goes here
def computer_move():
    move=-1
    # If I can win, others don't matter.
    for i in range(1,10):
        if make_move(board_values, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        # If player can win, block him.
        for i in range(1,10):
            if make_move(board_values, You, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for vi in moves:
            for mv in vi:
                if move == -1 and can_move(board_values, computer, mv):
                    move=mv
                    break
    return make_move(board_values, computer, move)

def space_exist():
    return board_values.count('X') + board_values.count('O') != 9

You, computer = select_char()
print('Player is [%s] and computer is [%s]' % (You, computer))
result='%%% DRAW ! %%%'
while space_exist():
    print_board()
    print('# Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board_values, You, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    if won:
        result='* Congratulations ! You won ! congo'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break;

print_board()
print(result)


# In[4]:


# python project 4
# simple rock paper scissors game
import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

        


# In[6]:


# python  project 5

#CHAT BOAT
from tkinter import *
window=Tk()
window.title("CHAT BOT")
window.geometry('650x500')
def catch():
    send="YOU->"+entry.get()
    chat.insert(END,"\n"+send)
    if(entry.get()=="hello"):
        chat.insert(END,"\n"+"BOT->Hi")
    elif(entry.get()=="glad to meet u!!"):
        chat.insert(END,"\n"+"BOT->my pleasure")
        chat.insert(END,"\n"+"BOT->How can i help u?")
    elif(entry.get()=="which is best python interpreter ?"):
        chat.insert(END,"\n"+"BOT->I THINK jupyter,pycharm,visual studios are quiet good")
    elif(entry.get()=="how many languages do u speak?"):
        chat.insert(END,"\n"+"BOT->At present only 1 language ")
    elif(entry.get()=="which is ur favorite programming language?"):
        chat.insert(END,"\n"+"BOT->Ofcourse python")  
    elif(entry.get()=="how to improve my coding skills?"):
        chat.insert(END,"\n"+"BOT->simple!! By writing codes from scratch ")     
    elif(entry.get()=="how to improve my coding skills?"):
        chat.insert(END,"\n"+"BOT->simple!! By writing codes from scratch ")
    elif(entry.get()=="bye bot"):
        chat.insert(END,"\n"+"BOT->bye have a nice day!! ")
    else:
        chat.insert(END,"\n"+"BOT->sorry i didn't get you!! ")    
    entry.delete(0,END)
chat=Text(window)
chat.grid(row=0,column=0,columnspan=3)
entry=Entry(window,width=100)
entry.grid(row=1,column=0)
bt=Button(window,text="SEND",command=catch).grid(row=1,column=1)
window.mainloop()


# In[ ]:




