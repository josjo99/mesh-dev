from django.db import models

# Create your models here.

class Channel(models.Model):
    channel_id= models.CharField(_("Channel Id"), max_length=50)
    channel_name= models.CharField(_("Channel Name"), max_length=50)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self):
        return self.name


class Group(models.Model):
    group_id= models.CharField(_("Group Id"), max_length=50)
    group_name= models.CharField(_("Group Name"), max_length=50)

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return self.name
