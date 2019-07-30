from django import forms
class LoginForm(forms.Form):
    u=forms.CharField()
    p=forms.CharField(widget=forms.PasswordInput)