import pandas as pd
import os
import re
from termcolor import colored
from logging_module import *


def inbox(user):
    # reading csv and counting New! tag
    os.chdir('allUsers')
    os.chdir(user)
    df = pd.read_csv(user + '.csv')
    c = df.loc[(df['status'] == 'New!')]
    # checking if inbox is empty or not
    if len(df) > 0:
        print(len(c), 'new message(s)\n')
        print(df)
        d = input('give an index to open the message or D/d for deleting ')
        # checking if input is number or not
        num_format = re.compile(r'^\-?[0-9][0-9]*$')
        it_is = re.match(num_format, d)
        if it_is:
            d = int(d)
            # checking if d exists or not
            if d < len(df):
                # for messages with sent tag
                if df.iloc[d, 2] == 'sent':
                    msg = df.iloc[d, 3]
                    print('message: ', msg)
                    print('u have sent this to', df.iloc[d, 1])
                # for messages with draft tag
                elif df.iloc[d, 2] == 'draft':
                    ans = input('send?')
                    if ans == 'y' or ans == 'Y':
                        # changing draft to sent and saving changes
                        df.iloc[d, 2] = 'sent'
                        df.to_csv(user + '.csv', index=False)
                        # finding receiver and message
                        receiver = df.iloc[d, 1]
                        message = df.iloc[d, 3]
                        # changing directory to receiver's
                        os.chdir('../../allUsers')
                        os.chdir(receiver)
                        # making a list of info, opening receiver's csv, appending and saving
                        receiver_list = [user, receiver, 'New!', message]
                        df_receiver = pd.read_csv(receiver + '.csv')
                        df_receiver.loc[len(df_receiver)] = receiver_list
                        df_receiver.to_csv(receiver + '.csv', index=False)
                        print('message has sent to', receiver, 'successfully')

                    elif ans == 'n' or ans == 'N':
                        print('lets return to main menu')
                # for messages with read or New! tag
                else:
                    # finding receiver
                    receiver = df.iloc[d, 0]
                    df.iloc[d, 2] = 'read'
                    df.to_csv(user + '.csv', index=False)
                    print('message: ', df.iloc[d, 3])
                    ans = input('reply this message? y/n')
                    if ans == 'y' or ans == 'Y':
                        message = input('ur message? ')
                        ans1 = input('message saved, inshaallah send dige? y/n')
                        if ans1 == 'y' or ans1 == 'Y':
                            # making a list of info, opening user's csv, appending and saving(receiver!)
                            user_list = [user, receiver, 'sent', message]
                            df.loc[len(df)] = user_list
                            df.to_csv(user + '.csv', index=False)
                            os.chdir('../../allUsers')
                            os.chdir(receiver)
                            # making a list of info, opening receiver's csv, appending and saving
                            receiver_list = [user, receiver, 'New!', message]
                            df_receiver = pd.read_csv(receiver + '.csv')
                            df_receiver.loc[len(df_receiver)] = receiver_list
                            df_receiver.to_csv(receiver + '.csv', index=False)
                            print('message has sent to', receiver, 'successfully')
                        # not sending the written message
                        elif ans1 == 'n' or ans1 == 'N':
                            user_list = [user, receiver, 'draft', message]
                            df.loc[len(df)] = user_list
                            df.to_csv(user + '.csv', index=False)
                    # not replying
                    elif ans == 'n' or ans == 'N':
                        print('ok onward to the main menu!')
                    # invalid input(neither y/Y nor n/N)
                    else:
                        text = colored('bro bro u make me angry ＼(｀0´)／', 'red')
                        print(text)
            # managing valid input(shouldn't be more than last index)
            elif d >= len(df):
                print('u really think i have that index noob? ┌( ಠ_ಠ)┘')
                os.chdir('../../../new test')
        # deleting
        else:
            if d == 'D' or d == 'd':
                # checking numeric input
                delete_ans = input('give an index to delete a message ')
                num_format = re.compile(r'^\-?[0-9][0-9]*$')
                it_is1 = re.match(num_format, delete_ans)
                if it_is1:
                    delete_ans = int(delete_ans)
                    df = df.drop(delete_ans)
                    df.to_csv(user + '.csv', index=False)
                    print('message deleted successfully')
                else:
                    print(' u did not enter an index for deleting')
            # not numeric nor d/D
            else:
                print('u didnt enter D/d or index')
    else:
        text = colored('''u r so lonely bro, ur inbox is empty  :-(  send someone a message!!''', 'blue')
        print(text)


def new_message(user, receiver):
    # checking valid receiver
    if receiver != user:
        # checking if receiver exists
        df = pd.read_csv('users_data.csv')
        c = df.loc[(df['username'] == receiver)]
        if len(c) == 1:
            message = input('user found, now enter ur message pls \n')
            answer = input('message saved, wanna send? (y/n or Y/N) \n')
            # writes info in user's file and saves
            if answer == 'y' or answer == 'Y':
                os.chdir('allUsers')
                os.chdir(user)
                user_list = [user, receiver, 'sent', message]
                df_user = pd.read_csv(user + '.csv')
                df_user.loc[len(df_user)] = user_list
                df_user.to_csv(user + '.csv', index=False)
            # changes dir to receiver's, writes info in user's file and saves
                os.chdir('../../allUsers')
                os.chdir(receiver)
                receiver_list = [user, receiver, 'New!', message]
                df_receiver = pd.read_csv(receiver + '.csv')
                df_receiver.loc[len(df_receiver)] = receiver_list
                df_receiver.to_csv(receiver + '.csv', index=False)
            # prints status
                print('message has sent to ', receiver)
                logger.info(f'{user} sent a message to {receiver}')
            # not sending the message
            # writes as draft and saves
            elif answer == 'n' or answer == 'N':
                os.chdir('allUsers')
                os.chdir(user)
                user_list = [user, receiver, 'draft', message]
                df_user = pd.read_csv(user + '.csv')
                df_user.loc[len(df_user)] = user_list
                df_user.to_csv(user + '.csv', index=False)
                print('has saved in draft box of', user)
            # managing invalid input(neither y/Y or n/N)
            else:
                print(' u entered the wrong format, now i am ANGRY (ಠ_ಠ)')
        # informing user about receiver
        else:
            print('receiver not found')
    # informing user not to message themselves
    else:
        text = colored('bro u cant text urself :/', 'yellow')
        print(text)

