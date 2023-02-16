from django.urls import path
from Alltable import User

urlpatterns =[
    path('add/',User.addUser),
]