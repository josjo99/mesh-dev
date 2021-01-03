from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MeshUserClass(models.Model):
    user_class_name = models.CharField("User Class", max_length=50)

    class Meta:
        verbose_name = "UserClass"
        verbose_name_plural = "UserClasses"

    def __str__(self):
        return self.name

class MeshUser(AbstractUser):
    userclass = models.ManyToManyField(MeshUserClass, verbose_name="User Class")
    
    class Meta:
        verbose_name = "MeshUser"
        verbose_name_plural = "MeshUsers"

    def __str__(self):
        return self.name