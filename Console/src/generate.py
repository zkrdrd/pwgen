import pyperclip, secrets
from src.next import next
import string

def generate(all:string) -> string:
    flag = False
    flage = False
    while not flag:
        length = int(input('\nEnter the length of password: '))
        if length <= 0: #isinstance(length, (int)): leght.isdigit()
            flag = False
            print ("\nLenght can't be below or equal to 0")
        else:
            flag = True
            while not flage:
                count = int(input('\nCoutn pasrwords (no more 30): '))
                if count == 1:
                    flage = True
                    password = "".join(secrets.choice(all) for i in range(length)) 
                    print('\nPassword -> %s' % password)
                    pyperclip.copy(password)
                    print ("The Password to be copied to the clipboard!")
                    next(all)
                elif count <= 30:
                    flage = True
                    for i in range(count):
                            print('Password -> %s' % "".join(secrets.choice(all) for i in range(length)))
                    next(all)
                else: 
                    print('\nCount can\'t be more 30.')
                    flage = False

