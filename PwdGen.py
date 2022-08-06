import secrets, string, sys

class Config(object):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

def settings():
    global all
    all = ""
    flag = False
    while not flag:
        lc = input("\nDo use lowercase? (Y,y/N,n)")
        if lc == "y" or lc == "Y":
            all = all + Config.lower
            flag = True
        elif lc == "N" or lc == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("\nIncorrect symbol\nWrite Y or N")
    flag = False
    while not flag:
        uc = input("\nDo use uppercase? (Y,y/N,n)")
        if uc == "y" or uc == "Y":
            all = all + Config.upper
            flag = True
        elif uc == "N" or uc == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("\nIncorrect symbol\nWrite Y or N")
    flag = False
    while not flag:
        digit = input("\nDo use digits? (Y,y/N,n)")
        if digit == "y" or digit == "Y":
            all = all + Config.num
            flag = True
        elif digit == "N" or digit == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("\nIncorrect symbol\nWrite Y or N")
    flag = False
    while not flag:
        sumbol = input("\nDo use punctuation? (Y,y/N,n)")
        if sumbol == "y" or sumbol == "Y":
            all = all + Config.symbols
            flag = True
        elif sumbol == "N" or sumbol == "n":
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
            flag = True


    #all = string.ascii_letters + string.digits + string.punctuation
    #passwd = "".join(random.sample(all,length))
    #print(passwd)

def app():
    print('\nWelcome to Password generator!')
    settings()
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
                generate(all)
            else: 
                print ("\nIncorrect symbol\nWrite Y or N")
        elif new == "N" or new == "n":
            print ("\nExit\n")
            sys.exit()
        else: 
            flag = True
            print ("\nIncorrect symbol\nWrite Y or N")


if __name__ == "__main__":
    app()

    
