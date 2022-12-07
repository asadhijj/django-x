from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    type = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.email