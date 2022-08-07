import secrets, string, sys, pyperclip

class Config(object):
    inputs = ["\nDo use lowercase? (Y,y/N,n) ", "\nDo use uppercase? (Y,y/N,n) ", "\nDo use digits? (Y,y/N,n) ", "\nDo use symbols? (Y,y/N,n) "]
    variables = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

def settings():
    global all
    all = ""
    for i,j  in zip(Config.inputs, Config.variables):
        flag = False
        while not flag:
            inp = input(i)
            if inp == "y" or inp == "Y":
                all = all + j
                flag = True
            elif inp == "N" or inp == "n":
                all = all
                flag = True
            else: 
                flag = False
                print ("\nIncorrect symbol\nWrite Y or N")
    return all

def generate(all):
    flag = False
    while not flag:
        length = input('\nEnter the length of password: ')
        if not length.isdigit(): #isinstance(length, (int)):
            flag = False
        else:
            length = int(length)
            password = "".join(secrets.choice(all) for i in range(length)) 
            print('\nPassword -> %s' % password)
            pyperclip.copy(password)
            print ("The Password to be copied to the clipboard!")
            flag = True

def check(all):
    if all == "": 
        print("\nError: All parameters in null!\nStart now.")
        settings()

def app():
    print('\nWelcome to Password generator!')
    settings()
    check(all)
    generate(all)
    flag = False
    while not flag:
        new = input('\nGenerate a new password? (Y,y/N,n)')
        if new == "y" or new == "Y":
            current = input('\nUse current settings? (Y,y/N,n)')
            if current == "y" or current == "Y":
                generate(all)
            elif current == "N" or current == "n":
                settings()
                check(all)
                generate(all)
            else:
                print ("\nIncorrect symbol\nWrite Y or N")
                flag = False
        elif new == "N" or new == "n":
            print ("\nExit\n")
            sys.exit()
        else: 
            flag = False
            print ("\nIncorrect symbol\nWrite Y or N")

if __name__ == "__main__":
    app()

    
