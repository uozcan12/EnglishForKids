#-*- coding:utf-8 -*-

from django.contrib import admin
from userprofile.models import UserProfile,Department

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','gender','title','department']
    list_filter=['gender','department']
    search_fields=['user__username','department__department_name']

@admin.register(Department)   
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name','manager']
    list_filter=['name']
    search_fields=['name','manager__username']

     

