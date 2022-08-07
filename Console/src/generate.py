import pyperclip, secrets
from src.next import next
def generate(all):
    flag = False
    while not flag:
        length = input('\nEnter the length of password: ')
        if not length.isdigit(): #isinstance(length, (int)):
            flag = False
            print ("\nIt's not a number")
        else:
            flag = True
            length = int(length)
            password = "".join(secrets.choice(all) for i in range(length)) 
            print('\nPassword -> %s' % password)
            pyperclip.copy(password)
            print ("The Password to be copied to the clipboard!")
            next(all)
