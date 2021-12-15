import re
import os
import csv
from csv import writer


class Sign_in:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def test(self):
        print('this will match info with da csv file')

class Sign_up:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def test(self):
        print('now u r registered ALAKI MASALN')
