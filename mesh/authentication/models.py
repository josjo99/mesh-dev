from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
#from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    #is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')

    class Meta():
        verbose_name = "User"
        verbose_name_plural = "Users"

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    #def has_perm(self, perm, obj=None):
        #return self.is_admin
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    #def has_module_perms(self, app_label):
        #return True


'''@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)'''