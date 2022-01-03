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
            for d in range(len(df)):
                if df.iloc[d, 0] == self.username:
                    row = d
                    string_to_hash = self.password
                    hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
                    password1 = hash_object.hexdigest()
                    if df.iloc[row, 1] == password1:
                        print('it works')
                    else:
                        print('wrong pass')
        else:
            print('username not found')



user1 = Register('jhg', '123').sign_in()