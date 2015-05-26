import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# if use this, other page model can be deleted
# class UserModel(models.Model):
#     # member_type = models.IntegerField(default=0)
#     tenant = models.ForeignKey(TenantModel)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.username


# class TenantModel(models.Model):
#     name = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.username