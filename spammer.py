import smtplib


class art(object):
    def banner():
        print("""\


  .-')     _ (`-.    ('-.     _   .-')    _   .-')       ('-.  _  .-')   
 ( OO ).  ( (OO  )  ( OO ).-.( '.( OO )_ ( '.( OO )_   _(  OO)( \( -O )  
(_)---\_)_.`     \  / . --. / ,--.   ,--.),--.   ,--.)(,------.,------.  
/    _ |(__...--''  | \-.  \  |   `.'   | |   `.'   |  |  .---'|   /`. ' 
\  :` `. |  /  | |.-'-'  |  | |         | |         |  |  |    |  /  | | 
 '..`''.)|  |_.' | \| |_.'  | |  |'.'|  | |  |'.'|  | (|  '--. |  |_.' | 
.-._)   \|  .___.'  |  .-.  | |  |   |  | |  |   |  |  |  .--' |  .  '.' 
\       /|  |       |  | |  | |  |   |  | |  |   |  |  |  `---.|  |\  \  
 `-----' `--'       `--' `--' `--'   `--' `--'   `--'  `------'`--' '--'



                                                    \n""")
    banner()   

class spammer(object):
    data = input("Press enter to start email spammer:")
    
    email = input("SENDER EMAIL:\n ")
    receiver_email = input("RECEIVER EMAIL:\n ")

    subject = input("SUBJECT: ")
    message = input("MESSAGE: ")

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, AppPassword)
    for i in range (100):
            server.sendmail(email, receiver_email, text)
