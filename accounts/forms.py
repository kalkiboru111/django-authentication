from django import forms 

class UserLoginForm(forms.Form):
    ''' Form users use to log themselves in '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)