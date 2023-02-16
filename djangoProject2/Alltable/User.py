import json

from.views import *

def do(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in['POST','DELETE']:
        request.params = json.loads(request.body)


    action = request.params['action']
    if action == 'list':
        return listUser(request)
    elif action == 'add':
        return addUser(request)
    elif action == 'del':
        return delUser(request)
    else:
        return JsonResponse({'ret':1,'msg':'不支持该Http请求'})