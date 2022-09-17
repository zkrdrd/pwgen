import sys
import string

def next(all:string)->string:
    from src.generate import generate
    from src.settings import settings
    flag = False
    while not flag:
        new = input('\nGenerate a new password? (Y,y/N,n) ')
        if new == "y" or new == "Y":
            current = input('\nUse current settings? (Y,y/N,n) ')
            if current == "y" or current == "Y":
                generate(all)
            elif current == "N" or current == "n":
                settings()
                generate(all)
            else:
                flag = False
                print ("\nIncorrect symbol\nWrite Y or N ")
        elif new == "N" or new == "n":
            print ("\nExit\n")
            sys.exit()
        else: 
            flag = False
            print ("\nIncorrect symbol\nWrite Y or N ")
