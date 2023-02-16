from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        request.session['usertype'] = user.lever
        request.session['name'] = user.first_name
        request.session['username'] = user.username
        return {'ret':0}
    else:
        return {'ret':1}
def signout(request):
    logout(request)
    return {'ret':0}