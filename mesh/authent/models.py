from django.db import models

# Create your models here.

class UserClass(models.Model):
    user_class_id = models.CharField("User Class Id", max_length=50)
    user_class_name = models.CharField("User Class Name", max_length=50)

    class Meta:
        verbose_name = "UserClass"
        verbose_name_plural = "UserClasses"

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.CharField("user_id", max_length=50)
    email = models.EmailField("Email", max_length=254)
    password = models.CharField("Password", max_length=50)
    user_class = models.OneToOneField("UserClass", verbose_name="User Class", on_delete=models.PROTECT)

    class Meta:
        verbose_name ="User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name