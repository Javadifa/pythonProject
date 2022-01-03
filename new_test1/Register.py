import re
import os
import pandas as pd
import hashlib
from logging_module import *


class Register:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count = 0

    def sign_in(self):
        # finding username
        df = pd.read_csv('users_data.csv')
        c = df.loc[(df['username'] == self.username)]
        # checking user with their pass
        if len(c) == 1:
            for d in range(len(df)):
                if df.iloc[d, 0] == self.username:
                    row = d
                    string_to_hash = self.password
                    hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
                    password1 = hash_object.hexdigest()
                    if df.iloc[row, 2] != 'NOK':
                        if df.iloc[row, 1] == password1:
                            print('logged in')
                            logger.info(f'{self.username} logged in successfully')
                            return True
                        else:
                            count = 1
                            print('wrong pass')
                            logger.info(f'{self.username} unsuccessful attempt to log in')
                            while count < 5:
                                ans = input('enter pass again: ')
                                string_to_hash = ans
                                hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
                                password1 = hash_object.hexdigest()
                                if df.iloc[row, 1] != password1:
                                    print('try again')
                                    count += 1
                                    print(3 - count, 'time(s) left')
                                    logger.info(f'{self.username} unsuccessful attempt to log in')
                                    if count == 3:
                                        df.iloc[row, 2] = 'NOK'
                                        df.to_csv('users_data.csv', index=False)
                                        print('ur account is banned now')
                                        logger.warning(f'{self.username} is blocked')
                                        return False
                                else:
                                    print('logged in')
                                    return True
                    else:
                        print('account is banned')
                        logger.warning(f'{self.username} is blocked but tried to log in')
        else:
            print('username not found')
            return False

    def sign_up(self):
        # checking unique username
        df = pd.read_csv('users_data.csv')
        c = df.loc[(df['username'] == self.username)]
        if len(c) >= 1:
            print('username is taken')
        else:
            # checking password with special pattern
            if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{7,}', self.password):
                print('done! now ur data is saved')
                logger.info(f'{self.username} just registered')
            else:
                print('password is weak but we accept it bcs we are KHASTEH!')
                # warning user
                logger.warning(f'password of user: {self.username} is weak, warn them')
            # hashing pass
            string_to_hash = self.password
            hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
            password1 = hash_object.hexdigest()
            # saving info in users_data.csv
            data = {'username': [self.username], 'password': [password1], 'log_in_status': 'ok'}
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

