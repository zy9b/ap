from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.


class User(AbstractUser):
    lever = models.PositiveIntegerField()
    REQUIRED_FIELDS = ['lever']
    class Meta:
        db_table="by_user"
    @staticmethod
    def add(data,usertype):
        try:
            username = data['username']
            if User.objects.filter(username=username).exists():
                return {'ret':1,'msg':f'用户{username}已存在'}
            user = User.objects.create(
                username=username,
                password = make_password(data['password']),
                lever = usertype
            )
            return {'ret':0,'name':user.username}
        except Exception as e:
            return {'ret':0,'msg':f'出现问题，请联系开发人员！错误信息:{e}'}
    @staticmethod
    def list():
        return {'ret':0,'list':list(User.objects.values())}
    @staticmethod
    def delUser(name):
        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            return{
            'ret':1,
            'msg':f'不存在名字为{name}的员工'
        }
        user.delete()
        return {'ret':0}
    @staticmethod
    def modifyUser(request,username,name):
        try:
            user = User.objects.get(username=username)
            user.username = name
            request.session['name'] = name
            user.save()
        except Exception as e:
            return {'ret':1,'msg':e}
        return {'ret':0}
class Order_number(models.Model):
    id = models.CharField(max_length=5,primary_key=True)
    @staticmethod
    def add(id):
        if id[0] is "K" and id[1]>='A' and id[1]<='D' and len(id)==5:
            Order_number.objects.create(
                id = id
            )
        else:
            return {'ret':1,'msg':'id不规范，请修改！'}
        return {'ret':0}
    @staticmethod
    def dels(id):
        try:
            order = Order_number.objects.get(id=id)
        except Exception as e:
            return {'ret':1,'msg':e}
        order.delete()
        return {'ret':0}
    @staticmethod
    def find(id):
        try:
            order = Order_number.objects.get(id = id)
        except Exception as e:
            return {'ret': 1, 'msg': e}
        return {'ret':0}
    @staticmethod
    def list():
        return {'ret':0,'list':list(Order_number.objects.values())}
class Model(models.Model):
    count = models.IntegerField()
    describe = models.CharField(max_length=800)
    delivery_date = models.DateField()
    logistics = models.IntegerField()
    order_number = models.ForeignKey(Order_number,on_delete=models.PROTECT)
    @staticmethod
    def add(count,describe,delivery_date,logistics,order_number):
        try:
            Model.objects.create(
                count=count,
                describe=describe,
                delivery_date=delivery_date,
                logistics=logistics,
                order_number=order_number,
            )
        except Exception as e:
            return {'ret':1,'msg':e}
        return {'ret':0}
    @staticmethod
    def dels(count,order_number):
        try:
            order = Model.objects.get(count=count,order_number=order_number)
        except Exception as e:
            return {'ret':1,'msg':e}
        order.delete()
        return {'ret':0}
    @staticmethod
    def find(count,order_number):
        try:
            order = Order_number.objects.get(count=count,order_number=order_number)
        except Exception as e:
            return {'ret': 1, 'msg': e}
        return {'ret':0,'order':order}
    @staticmethod
    def list():
        return {'ret':0,'list':list(Model.objects.values())}

