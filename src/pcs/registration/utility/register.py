"""
Register Utility
- add account or model to db
"""

from bcrypt import hashpw, gensalt
from registration.models import Account, Team
from registration.utility.passgen import makePassword

def addAccount(userInfo):
    user = Account(
        FirstName=userInfo['FirstName'],
        LastName=userInfo['LastName'],
        FsuID=userInfo['FsuID'],
        FsuNum=userInfo['FsuNum'],
        Email=userInfo['Email'],
        Password=hashpw(str(userInfo['Password']).encode(), gensalt()).decode(),
    )

    user.save()
    return user

def addTeam(teamInfo, leaderID, members):
    team = Team(
        TeamName=teamInfo['TeamName'],
        Division=teamInfo['Division'],
        Password=makePassword(),
        Leader_id=leaderID
    )

    team.save()
    return team
