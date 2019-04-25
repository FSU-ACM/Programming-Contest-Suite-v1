"""
Authentication Utility
- query db for user
- return user from db
- hash pass and assure it matches pass in db
"""

from bcrypt import hashpw, checkpw
from django.core.exceptions import ObjectDoesNotExist
from registration.models import Account


def getUser(req):
    """
    getUser
    - search db for email
    - returns user if they exists or None if they don't 
    """
    try:
        User = Account.objects.get(Email=req['Email'])
        return User
    except ObjectDoesNotExist:
        return None

def userExists(req):
    """
    userExists
    - return True if user is in db, False otherwise
    """
    if getUser(req) is not None:
        return True
    else:
        return False

def checkPass(req):
    """
    checkPass
    - if user is in db and hashed password matches the db return True, otherwise return False 
    """
    User = getUser(req)
    if User is not None and checkpw(str(req['Password']).encode(), str(User.Password).encode()):
        return True
    else:
        return False