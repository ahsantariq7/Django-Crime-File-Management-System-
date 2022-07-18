
from django.contrib import admin
from system.models import Contact
from system.models import Crime
from system.models import AddMissingPerson
from system.models import ShowMostWantedPerson
from system.models import FIR
from system.models import AddComplaint

# Register your models here.
admin.site.register(Contact)
admin.site.register(ShowMostWantedPerson)
admin.site.register(AddMissingPerson)
admin.site.register(FIR)
admin.site.register(AddComplaint)
admin.site.register(Crime)


