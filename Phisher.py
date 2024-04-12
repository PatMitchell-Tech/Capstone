"""
Wannaphish email sender program. This program is designed to help you send emails using smtplib and gmail to send emails. This program allows you to send emails containing malicious links
Author:Patrick Mitchell
Professor:Anup Parajuli
School: Lake Superior College
Warning: This program is for educational purposes only. Do not use this program for malicious purposes. I am not responsible for any outcomes of this program
"""



import smtplib#smtp library that allows you to send gmail through python

class phish(object):#This class is designed for phishing
    def banner():
        print("""
 _    _                               _     _     _    ___  
| |  | |                             | |   (_)   | |  |__ \ 
| |  | | __ _ _ __  _ __   __ _ _ __ | |__  _ ___| |__   ) |
| |/\| |/ _` | '_ \| '_ \ / _` | '_ \| '_ \| / __| '_ \ / / 
\  /\  / (_| | | | | | | | (_| | |_) | | | | \__ \ | | |_|  
 \/  \/ \__,_|_| |_|_| |_|\__,_| .__/|_| |_|_|___/_| |_(_)  
                               | |                          
                               |_|


                               """)
    banner()

    def starter():
        start = input("Press enter to start this program:\n")
    starter()

    

    
    
email = input("SENDER EMAIL:\n ")
receiver_email = input("RECEIVER EMAIL:\n ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, AppPassword)

server.sendmail(email, receiver_email, text)

print("This email has been sent to " + receiver_email)
