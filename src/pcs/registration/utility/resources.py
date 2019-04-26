from import_export import resources
from registration.models import Account


class AccountResource(resources.ModelResource):
    class Meta:
        model = Account
