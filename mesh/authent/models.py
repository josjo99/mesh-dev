from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT
# Create your models here.

class UserClass(models.Model):
    user_class_name = models.CharField("User Class", max_length=50,)

class User(AbstractUser):
    user_class = models.ManyToManyField(UserClass, verbose_name="User Class",on_delete=PROTECT)