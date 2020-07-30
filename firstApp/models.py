from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    class AddressFromNepal(models.TextChoices):
        GORKHA = 'GK', _('Gorkha')
        NEPALJUNG = 'NPJG', _('Nepaljung')
        KATHMANDU = 'KTM', _('Kathmandu')
        BUTWAL = 'BTW', _('Butwal')
        CHITWAN = 'CHW', _('Chitwan')

    first_name = models.CharField(max_length=50, default="Hari")
    last_name = models.CharField(max_length=50, default="Bahadur")
    nepal_address = models.CharField(
        max_length=4,
        choices=AddressFromNepal.choices,
        default=AddressFromNepal.KATHMANDU,
        db_column="home_address",
        db_index=True
    )
    cv = models.FileField(upload_to='uploads/', null=True)
    car = models.ForeignKey("Car", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Car(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person,
                                     through='Membership',
                                     through_fields=('group', 'person'),
                                     )

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
        null=True
    )

    def __str__(self):
        return f"{self.person} in {self.group}"
