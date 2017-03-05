from django import forms

class loginform(forms.Form):
    uname=forms.CharField(label='uname', max_length=30)
    passw=forms.CharField(label='pass', max_length=20, widget=forms.PasswordInput)
