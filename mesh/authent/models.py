from django.db import models

# Create your models here.

class UserClass(models.Model):
    user_class_id = models.CharField(_("User Class Id"), max_length=50)
    user_class_name = models.CharField(_("User Class Name"), max_length=50)

    class Meta:
        verbose_name = _("UserClass")
        verbose_name_plural = _("UserClasses")

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.CharField(_("user_id"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    password = models.CharField(_("Password"), max_length=50)
    user_class = models.OneToOneField(".UserClass", verbose_name=_("User Class"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name