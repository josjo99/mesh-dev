from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserClass(models.Model):
    user_class_name = models.CharField("User Class", max_length=50)

    class Meta:
        verbose_name = "UserClass"
        verbose_name_plural = "UserClasses"

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    user_class = models.ManyToManyField(UserClass, verbose_name="User Class")
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
