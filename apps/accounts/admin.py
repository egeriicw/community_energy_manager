from django.contrib import admin

from apps.accounts.models import Property
from apps.accounts.models import Account
from apps.accounts.models import Meter
from apps.accounts.models import PropertyType
from apps.accounts.models import Address
from apps.accounts.models import Parcel


# Register your models here.

admin.site.register(Property)
admin.site.register(Account)
admin.site.register(Meter)
admin.site.register(PropertyType)
admin.site.register(Address)
admin.site.register(Parcel)
