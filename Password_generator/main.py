import secrets
from pyfiglet import Figlet
import os
import string
import colored
os.system('cls')

name = '''
r a m i x   G u a r d
'''
f = Figlet(font='epic',width= 150)
ascii_art = f.renderText(name)
print(ascii_art)
print('{0:>110}'.format("Password generator"))
print('{0:>108}'.format("Version 1.0.0"))
print('''
[+]Made by ramix[+]
Instagram : https://instagram.com/ramixcode?igshid=ZGUzMzM3NWJiOQ==
Telegram : https://t.me/Theramix
Github : https://github.com/ramixcode
''')

check_num_of_password_digit = 0
check_need_sym = 0
check_need_num = 0
check_do_not_show_sure_sym = 0
do_not_show_sure_sym = 0
check_do_not_show_sure_num = 0
do_not_show_sure_num = 0
password_gen = []
        
while True:
    try:
        if check_num_of_password_digit == 0:
            num_of_password_digit = int(input("How many digits should the password be?(It is better to be more than 8 digits):"))
            check_num_of_password_digit = 1

            if num_of_password_digit < 4:
                check_num_of_password_digit = 0
                print("The number of digits is at least 4!!!")
                continue

        if check_need_sym == 0:
            need_sym = int(input(
                "Do you need symbols in your password?\n1)yes, i need\n2)No, I don't need it\n==>"
                ))
            check_need_sym = 1
            if need_sym == 2:
                if check_do_not_show_sure_sym == 0:
                    print("Alert!!!\nSymbols make passwords impenetrable, if they are not in your password, the security of your password will decrease")
                    sure_sym = int(input("Are you sure you don't need symbols?\n1)Yes, i\'m sure\n2)No, I want to change it\n==>"))
                    
                    if sure_sym ==  1:
                        do_not_show_sure_sym = int(input("Don\'t show this warning again?\n1)Yes, Don\'t show again\n2)No, show it next time\n==>"))
                        if do_not_show_sure_sym == 1:
                            check_do_not_show_sure_sym = 1
                        if do_not_show_sure_sym == 2:
                            check_do_not_show_sure_sym = 0
                        

                    if sure_sym == 2:
                        need_sym = 1
                        continue
                     
            
        if check_need_num == 0:
            need_num = int(input(
                "Do you need number in your password?\n1)yes, i need\n2)No, I don't need it\n==>"
                ))
            
            if need_sym == 1 and need_num == 1:
                characters = string.ascii_letters + string.digits + string.punctuation

                for i in range(0, num_of_password_digit):
                    first_choice = secrets.choice(characters)
                    password_gen.append(first_choice)
                    
                password_finaly = ''.join(password_gen)
                print(password_finaly)

            if need_num == 1 and need_sym == 2:
                characters = string.ascii_letters + string.digits 

                characters = string.ascii_letters + string.digits + string.punctuation

                for i in range(0, num_of_password_digit):
                    first_choice = secrets.choice(characters)
                    password_gen.append(first_choice)
                    
                password_finaly = ''.join(password_gen)
                print(password_finaly)

            if need_num == 2 and need_sym == 1:
                characters = string.ascii_letters + string.punctuation

                for i in range(0, num_of_password_digit):
                    first_choice = secrets.choice(characters)
                    password_gen.append(first_choice)
                    
                password_finaly = ''.join(password_gen)
                print(password_finaly)

            if need_num == 2 and need_sym == 2:
                characters = string.ascii_letters
                
                for i in range(0, num_of_password_digit):
                    first_choice = secrets.choice(characters)
                    password_gen.append(first_choice)
                    
                password_finaly = ''.join(password_gen)
                print(password_finaly)

        check_num_of_password_digit = 0
        check_need_sym = 0
        check_need_num = 0
        check_do_not_show_sure_sym = 0
        do_not_show_sure_sym = 0
        check_do_not_show_sure_num = 0
        do_not_show_sure_num = 0
                
                                           
    except ValueError as error:
        print('Please insert the correct entry!!!')