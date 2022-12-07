from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class cars(models.Model):
     type = models.CharField(max_length=64)
     car_model = models.CharField(max_length=64)
     purchaser =models.ForeignKey(CustomUser, on_delete = models.CASCADE)

     def __str__(self):
        return self.type

     def get_absolute_url(self):
        return reverse('cars-list')
