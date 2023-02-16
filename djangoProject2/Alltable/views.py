from django.http import JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def addUser(request):
    data = request.param_dict['data']
    ret = User.add(data,request.param_dict['type'])
    return JsonResponse(ret)
def listUser(request):
    return User.list()
def delUser(request):
    return User.delUser(request.param_dict['name'])