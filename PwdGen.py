import secrets, string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = ""

def settings():
    global all
    flag = False
    while not flag:
        lc = input("Do use lowercase? (Yes,y/No,n)")
        if lc == "Yes" or lc == "YEs" or lc == "YES" or lc == "yES" or lc == "yeS" or lc == "yes" or lc == "yEs" or lc == "y" or lc == "Y":
            all = all + lower
            flag = True
        elif lc == "No" or lc == "NO" or lc == "nO" or lc == "N" or lc == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("Incorrect symbol")
    flag = False
    while not flag:
        uc = input("Do use uppercase? (Yes,y/No,n)")
        if uc == "Yes" or uc == "YEs" or uc == "YES" or uc == "yES" or uc == "yeS" or uc == "yes" or uc == "yEs" or uc == "y" or uc == "Y":
            all = all + upper
            flag = True
        elif uc == "No" or uc == "NO" or uc == "nO" or uc == "N" or uc == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("Incorrect symbol")
    flag = False
    while not flag:
        digit = input("Do use digits? (Yes,y/No,n)")
        if digit == "Yes" or digit == "YEs" or digit == "YES" or digit == "yES" or digit == "yeS" or digit == "yes" or digit == "yEs" or digit == "y" or digit == "Y":
            all = all + num
            flag = True
        elif digit == "No" or digit == "NO" or digit == "nO" or digit == "N" or digit == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("Incorrect symbol")
    flag = False
    while not flag:
        sumbol = input("Do use punctuation? (Yes,y/No,n)")
        if sumbol == "Yes" or sumbol == "YEs" or sumbol == "YES" or sumbol == "yES" or sumbol == "yeS" or sumbol == "yes" or sumbol == "yEs" or sumbol == "y" or sumbol == "Y":
            all = all + symbols
            flag = True
        elif sumbol == "No" or sumbol == "NO" or sumbol == "nO" or sumbol == "N" or sumbol == "n":
            all = all
            flag = True
        else: 
            flag = False
            print ("Incorrect symbol")
    return all

def generate(all):
    length = int(input('\nEnter the length of password: '))
    password = "".join(secrets.choice(all) for i in range(length)) 
    print(password)

    #all = string.ascii_letters + string.digits + string.punctuation
    #passwd = "".join(random.sample(all,length))
    #print(passwd)

print('Welcome to Password generator!')
settings()
generate(all)
