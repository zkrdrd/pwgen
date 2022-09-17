from src.generate import generate
from src.Config import Config
import string

def settings() -> string:
    global all
    all = ""
    for i,j  in zip(Config.inputs, Config.variables):
        flag = False
        while not flag:
            inp = input(i)
            if inp == "y" or inp == "Y":
                flag = True
                all = all + j
            elif inp == "N" or inp == "n":
                flag = True
                all = all
            else: 
                flag = False
                print ("\nIncorrect symbol\nWrite Y or N")
    if all == "": 
        print("\nError: All parameters in null!\nStart now.")
        settings()
    else: 
        generate(all)