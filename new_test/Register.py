import re
import os
import pandas as pd
import hashlib
from logging_module import *


class Register:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.access = False

    def sign_in(self):
        # finding username
        df = pd.read_csv('users_data.csv')
        c = df.loc[(df['username'] == self.username)]
        # if username existed
        if len(c) == 1:
            print('username found')
            # matching entered pass with hashed one
            string_to_hash = self.password
            hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
            password1 = hash_object.hexdigest()
            # finding pass
            d = df.loc[(df['password'] == password1)]
            if len(d) >= 1:
                print('logged in! ')
                logger.info(f'{self.username} logged in')
                # access for messenger menu(main file)
                self.access = True
            else:
                print('wrong pass')
                logger.info(f'{self.username} could not sign in due to wrong password')

        elif len(c) != 1:
            print('user not found')

    def sign_up(self):
        # checking unique username
        df = pd.read_csv('users_data.csv')
        c = df.loc[(df['username'] == self.username)]
        if len(c) >= 1:
            print('username is taken')
        else:
            # checking password with special pattern
            if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', self.password):
                print('done! now ur data is saved')
                logger.info(f'{self.username} just registered')
            else:
                print('password is weak but we accept it bcs we are KHASTEH!')
                # warning user
                logger.warning(f'password of user: {self.username} is weak, warn him')
            # hashing pass
            string_to_hash = self.password
            hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
            password1 = hash_object.hexdigest()
            # saving info in users_data.csv
            data = {'username': [self.username], 'password': [password1]}
            df1 = pd.DataFrame(data)
            df1.to_csv('users_data.csv', mode='a', index=False, header=False)
            # creating user's directory and their csv file
            os.chdir('allUsers')
            os.mkdir(self.username)
            os.chdir(self.username)
            df2 = pd.DataFrame({'from': [], 'to': [], 'status': [], 'message': []})
            df2.to_csv(self.username + '.csv', index=False)
            # back to project's main folder
            os.chdir('../../../new test')

