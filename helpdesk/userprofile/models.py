#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=128)
    manager = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Birim"
        verbose_name_plural = "Birimler"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    GENDER = (('K', 'Kadin'), ('E', 'Erkek'))
    gender = models.CharField(choices=GENDER, max_length=1)
    title = models.CharField(max_length=40)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = "Kullanıcı Profili"
        verbose_name_plural = "Kullanıcı Profilleri"



