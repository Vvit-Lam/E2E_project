from django.contrib.auth.models import AbstractUser
from django.db import models

class Userr(AbstractUser):
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
