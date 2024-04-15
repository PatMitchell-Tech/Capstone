---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Disclaimer: These pieces of software are for Educational purposes only. I am in no way responsible for the outcomes these programs may or may not produce. Do not use for Malicious purposes.

My capstone project is based around malware research, development, data recovery, and learning how to mitigate risks from threat actors

In my project I have created many different types of malware such as: Keyloggers, winlockers, SSH brute force tool, and a Program for Phishing/email spamming.

Not all of the code used in these programs are originally written by me and I will give credit to the original developer(s) in those respective programs.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
This page will be updated closer to the end of my current capstone project                                                                                           
                                                                                                                                                                     
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Radius.py dependencies: pynput module                                                                                                                                
                                                                                                                                                                     
To perform this on windows type pip install pynput into cmd or powershell. If you are on linux type into your terminal: sudo apt install python3-pynput              

sshbruter.py dependencies: passwords.csv 

You need to match the .csv file to the list file in the sshbruter.py program. You will also need to put a list of usernames in the first section and then passwords 
in the second. Example:

![image](https://github.com/PatMitchell-Tech/Capstone/assets/120431122/bc63f4fc-4966-4b02-9cf9-040e242b4422)



---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Feel free to use and modify this code for educational purposes. I'm not responsible for the outcomes these programs may or may not have.

I wouldn't recommend running these programs on bare metal. Instead I would recommend running these scripts on a virtual machine.

These scripts for the most part will not do any serious damage to your systems but it is better to be safe than sorry with programs of this nature.
