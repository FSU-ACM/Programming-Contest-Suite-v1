# simple method to generate passwords
# Intended for use as pass gen for teams in DOMJudge

import random

def makePassword():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''

    for c in range(8): # Sets length of password
        password += random.choice(chars)

    return password
