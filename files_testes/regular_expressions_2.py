'''
Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.
'''
import re

def strongpasswd(password):
    if len(password) >=  8 \
    and re.search("^[a-zA-Z0-9]+", password) \
    and re.search("[a-z]+", password) \
    and re.search("[A-Z]+", password) \
    and re.search("[0-9]+", password) \
    and re.search("[@_!#$%^&*()<>?/\|}{~:]+", password):
        print(password, True)
        return True
    else:
        print(password, False)
        return False

strongpasswd('12345aF18@')
strongpasswd('asdfgH1jk1')
strongpasswd('asDf$##r4')
strongpasswd('123$%Adf12')
strongpasswd('asdadsfasd1')
