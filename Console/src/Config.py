import string

class Config(object):
    inputs = ["\nDo use lowercase? (Y,y/N,n) ", "\nDo use uppercase? (Y,y/N,n) ", "\nDo use digits? (Y,y/N,n) ", "\nDo use symbols? (Y,y/N,n) "]
    variables = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

