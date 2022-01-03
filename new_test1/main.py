import os
from termcolor import colored
import Register as rG
import messenger as msg
from logging_module import *


# defining menus
def register_menu():
    text = colored('(　-_･) ︻デ═一  ▸ - -  (✖╭╮✖)', 'magenta')
    print(text)
    text1 = colored('[1] sign in', 'cyan')
    print(text1)
    text2 = colored('[2] sign up', 'cyan')
    print(text2)
    text3 = colored('[3] exit', 'cyan')
    print(text3)


def messenger_menu():
    text1 = colored('[1] inbox','magenta')
    print(text1)
    text2 = colored('[2] new message', 'magenta')
    print(text2)
    text3 = colored('[3] return', 'magenta')
    print(text3)


register_menu()
option = input('enter ur option ')

while option != '3':
    if option == '1':
        username = input('username? ')
        password = input('password? ')
        # giving access to messenger's menu
        if rG.Register(username, password).sign_in():
            print('welcome to our messenger NOOB!')
            messenger_menu()
            option1 = input('now where to go?')
            while option1 != '4':
                if option1 == '1':
                    msg.inbox(username)
                    messenger_menu()
                    # absolute addressing
                    os.chdir('C:/Users/Yugi/Desktop/new test')
                    option1 = input('now where to go?')

                elif option1 == '2':
                    receiver = input('dabsh who is ur receiver? ')
                    msg.new_message(username, receiver)
                    # absolute addressing
                    os.chdir('C:/Users/Yugi/Desktop/new test')
                    messenger_menu()
                    option1 = input('now where to go? ')

                elif option1 == '3':
                    logger.info(f'{username} logged out')
                    option1 = '4'

                else:
                    print('bro am i a joke to u?')
                    messenger_menu()
                    option1 = input('now where to go? ')
        else:
            print('no access to our messenger hehe, try again NOOB! :))) ')

    elif option == '2':
        username1 = input('username? ')
        password1 = input('password? ')
        rG.Register(username1, password1).sign_up()
    else:
        print('invalid option')

    print()
    register_menu()
    option = input('enter ur option ')


