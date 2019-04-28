"""
Validator Utility
"""

from django.core.exceptions import ObjectDoesNotExist
from registration.models import Account, Team

def validTeamName(req):
    """
    Valid Team Name
    - returns False if Team Name is already taken, True otherwise
    """
    return collision(req, model='team', identifier='name')


def availableFSUNum(req):
    """
    Available FSU Num
    - returns False if FSU Num is already linked to an account, True otherwise
    """
    return collision(req, model='account', identifier='num')

def validFSUNum(req):
    """
    Valid FSU Num
    - returns False if FSU Num contains characters, True otherwise
    """
    return str(req['FsuNum']).isdigit()

def validFSUID(req):
    """
    Valid FSU ID
    - returns False if FSU ID is already linked to an account, True otherwise
    """
    return collision(req, model='account', identifier='id')


def collision(req, model=None, identifier=None):
    """
    Collision Utility
    @param req: POST dictionary of form fields
    @param model: str of model you'd like to query the db for
    @param identifier: str of identifier you'd like to query the db for
    """
    if model is None or identifier is None:
        raise ValueError('Need valid parameters')
    if model == 'account':
        if identifier == 'num':
            try:
                obj = Account.objects.get(FsuNum=req['FsuNum'])
                return False
            except ObjectDoesNotExist:
                return True
        elif identifier == 'id':
            try:
                obj = Account.objects.get(FsuID=req['FsuID'])
                return False
            except ObjectDoesNotExist:
                return True
        else:
            raise ValueError('Need valid parameters')
    elif model == 'team':
        if identifier == 'name':
            try:
                obj = Team.objects.get(TeamName=req['TeamName'])
                return False
            except ObjectDoesNotExist:
                return True