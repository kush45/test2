from django.db import models

# Create your models here.
from django.db import models


class Register(models.Model):

    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return "{} ".format(self.username)

