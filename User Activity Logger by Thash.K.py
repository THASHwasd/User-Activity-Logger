# DISCLAIMER: This script is an educational project created by a 15-year-old developer.
#             The purpose is to demonstrate how to log user actions and their public IP address to a local file.
#             The IP address is logged locally and is not sent to external servers.
#             Users are responsible for ensuring the ethical use of this script in their environments.
#             
# NOTE: To disable IP logging, remove all code marked as 'IP MODULE' or refer to the README file.
#       The developer assumes no responsibility for any misuse of this code.
#             
# Explicitly for Educational Purposes Only.



import requests        # IP MODULE - Remove to remove IP logging 

Uptime = True
from datetime import datetime
import os


def get_public_ip():   # IP MODULE - Remove to remove IP logging 
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        public_ip = response.json().get('ip')
        return public_ip
    except requests.RequestException as e:
        return f"An error occurred: {e}"


# Main Program

User_list = ["example_user_1@domain.com" , "example_user_2@domain.com" , "example_user_3@domain.com"]  # Edit to include users
unregistered_user = ["example_unreg_user@domain.com" , "example_unreg_user1@domain.com"]  # Edit to include unregistered users

default_password = os.getenv("DEFAULT_PASSWORD", "QWERTY")  # Fallback to ('QWERTY'-Change if required) if the variable is not set - Setup enviromental variable through terminal (RECOMMENDED TO WATCH A VIDEO IF NEVER DONE BEFORE)
                                                            # not requiring hardcoded passwords

while Uptime == True: 
    user = input("Email: ")
    password = input("Password: ")

    if user in User_list and password == default_password:  # Enviromental Variable
        print("You have sucessfully logged in")
        
        f = open(r"user_log.txt", "a")  # Replace "user_log.txt" with your desired .txt file path
        current_time = datetime.now()
        f.write(f"{current_time.strftime('%d/%m/%Y %H:%M:%S')}  Public IP [{get_public_ip()}] USER SUCCESSFUL LOGIN    [{user}] \n") # IP MODULE - Remove {get_public_ip()}
        f.close() 
        
        print("Public IP Address:", get_public_ip())  # IP MODULE - Remove get_public_ip()
        
                                                                                    
    elif  user in unregistered_user:
        print(f"{user} has now been registered,")
        print(f"Your Password is: {default_password}")  # Enviromental Variable 
        print("Please relog in")


    elif user in User_list or password == default_password:  # Enviromental Variable
        print("Incorrect Password / Email")
        f = open(r"user_log.txt", "a")  # Replace "user_log.txt" with your desired .txt file path
        current_time = datetime.now()
        f.write(f"{current_time.strftime('%d/%m/%Y %H:%M:%S')}  Public IP [{get_public_ip()}] USER UNSUCCESSFUL LOGIN    [{user}]\n")  # IP MODULE - Remove {get_public_ip()}
        f.close()     

        unregistered_user.remove(user)
        User_list.append(user)

        f = open(r"user_log.txt", "a")  # Replace "user_log.txt" with your desired .txt file path, to log logins
        current_time = datetime.now()
        f.write(f"{current_time.strftime('%d/%m/%Y %H:%M:%S')}  Public IP [{get_public_ip()}] USER REGISTERED    [{user}]\n")  # IP MODULE - Remove {get_public_ip()}
        f.close()    


    else:
        print("You are not registered to use this service")
        print(f"Your IP has been logged [{get_public_ip()}]") # IP MODULE - Remove {get_public_ip()}
        f = open(r"user_log.txt", "a")  # Replace "user_log.txt" with your desired .txt file path
        current_time = datetime.now()
        f.write(f"{current_time.strftime('%d/%m/%Y %H:%M:%S')}  Public IP [{get_public_ip()}] USER UNAUTHORISED LOGIN    [{user}] \n")  # IP MODULE - Remove {get_public_ip()}
        f.close()  
