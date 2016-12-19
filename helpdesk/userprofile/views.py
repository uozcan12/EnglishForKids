#! -*- coding:utf-8-*-

from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from forms import UserForm,UserProfileForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# @csrf_exempt
def login(request):
    data={}
    data.update(csrf(request))
    note=None
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            user_login(request,user)
            return redirect('index')
        note = "Giriş başarısız" 
    data['note']=note
    return render_to_response("login.html",data)

@login_required
def update_profile(request):
    data={}
    user_form=UserForm(instance=request.user,prefix='user_form')
    try:
        userprofile_form=UserProfileForm(instance=request.user.userprofile,prefix='userprofile_form')
    except ObjectDoesNotExist :
        userprofile_form=UserProfileForm(prefix='userprofile_form')
    if request.POST :
        try:
            userprofile_form=UserProfileForm(request.POST, instance=request.user.userprofile,prefix='userprofile_form')
        except:
            
            userprofile_form=UserProfileForm(request.POST,prefix='userprofile_form')
            user_form=UserForm(request.POST,instance=request.user, prefix='user_form')
        if all([userprofile_form.is_valid(), user_form.is_valid()]):
            user=user_form.save()
            userprofile=userprofile_form.save(commit=False)
            userprofile.user=user
            user.save()
            return redirect("update_profile")
    data['userprofile_form']=userprofile_form
    data['user_form']=user_form  
    return render(request,'user_profile.html',data)  
@login_required
def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse('login'))