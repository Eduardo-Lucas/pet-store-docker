from django.db import models
from django.contrib.auth.admin import User


class Tutor(User):
    class Meta:
        proxy = True
