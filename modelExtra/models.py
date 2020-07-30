from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_my_age(age):
    if age < 20:
        raise ValidationError("Age should be more or equals to 20")


class UserBio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[validate_my_age])

    bio = models.CharField(max_length=200, blank=True)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.full_clean()
    #     return super.save()

    def clean(self):
        if self.age > 40:
            if not self.bio:
                raise ValidationError("Bio is required for age > 40")

    def __str__(self):
        return self.name
