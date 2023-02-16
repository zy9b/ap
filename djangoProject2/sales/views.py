from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .sign_in_out import *
from Alltable.models import User
# Create your views here.
def logins(request):
    if request.method == 'POST':
        back = signin(request)
        if back['ret'] == 1:
            messages.success(request,"用户名或密码错误")
        else:
            return HttpResponseRedirect('/')
    return render(request,'index/sgin.html')
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        print(request.POST)
        signout(request)
        return HttpResponseRedirect('/login')
    print(request.session['name'])
    return render(request,"index/index.html",context={'username':request.session['name'],'lever':request.session['usertype']})
def setting(request):
    if request.method == 'POST':
        User.modifyUser(request,request.session['username'],request.POST.get('first_name'))
    return render(request,"index/setting.html")