#! -*-coding:utf-8 -*-
'''
Created on 1 Şub 2016

@author: ugur
'''


from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
   # return HttpResponse("MERHABA DÜNYA")
   
   return render(request,"index.html")
    

