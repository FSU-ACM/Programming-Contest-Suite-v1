"""
Register Utility
- add account or model to db
"""

from functools import reduce
from bcrypt import hashpw, gensalt
from registration.models import Account, Team, Course
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
    
    if 'Courses' in userInfo.keys():
        for x in userInfo['Courses']:
            course = Course.objects.get(CourseID=x)
            user.course.add(course)

    user.save()
    return user

def addTeam(teamInfo, leaderID, memInfo, numMembers=1):
    memID, members = zip(*memInfo)
    
    team = Team(
        TeamName=teamInfo['TeamName'],
        Division=teamInfo['Division'],
        Members=reduce((lambda x,y: x+'\n'+y), list(members)),
        MemberIDs=reduce((lambda x,y: str(x)+','+str(y)), list(memID)),
        Count=numMembers,
        Password=makePassword(),
        Leader_id=leaderID
    )

    team.save()
    return team
