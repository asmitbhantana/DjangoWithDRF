from django.db import models

# Create your models here.
class ClassBasedModel(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()

    bio = models.TextField()

    def __str__(self):
        return self.first_name