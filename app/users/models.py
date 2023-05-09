# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_veterinarian = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
