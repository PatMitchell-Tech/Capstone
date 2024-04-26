---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Disclaimer: These pieces of software are for Educational purposes only. I am in no way responsible for the outcomes these programs may or may not produce. Do not use for Malicious purposes.

My capstone project is based around malware research, development, data recovery, and learning how to mitigate risks from threat actors

In my project I have created many different types of malware such as: Keyloggers, winlockers, SSH brute force tool, Automated phishing/email spamming program, and a Ransomware program.

All of these programs were created in the python programming language.

Not all of the code used in these programs are originally written by me and I will give credit to the original developer(s) in those respective programs.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
These PoC programs are designed to research the methods threat actors use to exploit systems. The goal of this project was to learn how to mitigate risks
associated with threat actors and the methods they use to exploit systems. Throughout this project I learned how to research and develop malware, perform hands on digital 
forensics, hunt for threats, find IoCs, analyze malware, and perform recovery on malware infected endpoints. This project taught me how to defend and attack systems as 
well as how to actively quaratine systems infected with malware.
                                                                                                                                                                     
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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
