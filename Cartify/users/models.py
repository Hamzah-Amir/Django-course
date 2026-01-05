from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']