import Register
import messenger

while True:
    b = input("wlc to our python messenger, do u have an account? (Y/N) ")

    if b =='Y':
        username1 = input('username? ')
        password1 = input('password? ')
        user1 = Register.Sign_in(username1, password1).test()
        a = input('''now where to go?
                sentBox, inbox, draft or new message?''')
        option = messenger.Messenger(a).test()


    if b == 'N':
        print('so u must register now')
        username1 = input('username? ')
        password1 = input('password? ')
        user1 = Register.Sign_up(username1, password1).test()
