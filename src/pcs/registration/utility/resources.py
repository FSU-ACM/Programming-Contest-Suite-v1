from import_export import resources
from registration.models import Account, Team


class AccountResource(resources.ModelResource):
    class Meta:
        model = Account


class TeamResource(resources.ModelResource):
    class Meta:
        model = Team
        fields = ('TeamName', 'Password')


def ExportCSV(choice):
    """
    ExportCSV takes in a string "Account" or "Team" to create and export
    a CSV file with the information required by the user.

    * Needs to include error checking to report if wrong string is entered

    """
    if choice == "Team":
        dataset = TeamResource().export()
        file = open("teams.csv", "w")
    else:
        dataset = AccountResource().export()
        file = open("accounts.csv", "w")

    file.write(dataset.csv)
    file.close
