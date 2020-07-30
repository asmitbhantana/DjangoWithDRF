from django.contrib import admin

# Register your models here.
from firstApp.models import Person, Membership, Group, Car

admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Group)
admin.site.register(Car)
