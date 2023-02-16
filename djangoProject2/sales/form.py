from django import forms
class user(forms.Form):
    first_name = forms.CharField(label='名字',max_length=100)