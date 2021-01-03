from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser,Group

# Create your models here.
'''
class UserClass(models.Model):
    user_class_id = models.CharField("User Class Id", max_length=50)
    user_class_name = models.CharField("User Class Name", max_length=50)

    class Meta:
        verbose_name = "UserClass"
        verbose_name_plural = "UserClasses"

    def __str__(self):
        return self.name
'''

class User(AbstractUser):
    user_groups = models.ManyToManyField("Group", verbose_name="User Groups")

    class Meta:
        verbose_name ="User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name