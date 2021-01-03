from django.db import models

# Create your models here.

class UserClass(models.Model):
    userclassname = models.CharField("UserClassName", max_length=50)

    class Meta:
        verbose_name = "UserClass"
        verbose_name_plural = "UserClasses"
    
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField("Email", max_length=254)
    password = models.CharField("Password",max_length=50)
    userclass = models.ManyToManyField("UserClass", "UserClass")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
