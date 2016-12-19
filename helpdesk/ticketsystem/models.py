#! -*- coding:utf-8-*-
from django.db import models
from userprofile.models import Department,UserProfile
from datetime import datetime


from userprofile.models import Department, UserProfile



# Create your models here.
class Priority(models.Model):
    name=models.CharField(max_length=32)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Öncelik"
        verbose_name_plural="Öncelikler"
    
        
class Status(models.Model):
    name=models.CharField(max_length=32)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="İş durum"
        verbose_name_plural="İş durumları"
    
class Product(models.Model):
    name=models.CharField(max_length=64)
    department=models.ForeignKey(Department)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Hizmet"
        verbose_name_plural="Hizmetler"
        
class Ticket(models.Model) :
    department=models.ForeignKey(Department)
    creator=models.ForeignKey(UserProfile)
    title=models.CharField(max_length=128)
    description=models.TextField(max_length=1000)
    priority=models.ForeignKey(Priority)
    status=models.ForeignKey(Status)
    create_date=models.DateTimeField(default=datetime.now())
    product=models.ForeignKey(Product)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="İş"
        verbose_name_plural="İşler"
    
class FollowUp(models.Model):
    ticket=models.ForeignKey(Ticket)
    followupnote=models.CharField(max_length=1000)
    followup_date=models.DateTimeField(default=datetime.now())
    followup_user=models.ForeignKey(UserProfile,related_name='followup_user')
    assigned_user=models.ForeignKey(UserProfile,related_name='assigned_user')