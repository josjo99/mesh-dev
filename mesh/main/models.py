from django.db import models

# Create your models here.

class Channel(models.Model):
    channel_id= models.CharField("Channel Id", max_length=50)
    channel_name= models.CharField("Channel Name", max_length=50)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name


class Group(models.Model):
    group_id= models.CharField("Group Id", max_length=50)
    group_name= models.CharField("Group Name", max_length=50)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name
