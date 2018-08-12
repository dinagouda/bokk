from django import forms

class userregister(forms.Form):
    f_name=forms.CharField(required =True ,widget=forms.TextInput( ))
    L_name = forms.CharField(required=True, widget=forms.TextInput( ))
    email = forms.CharField(required=True, widget=forms.TextInput())
    age= forms.CharField(required=True, widget=forms.TextInput( ))
    password=forms.CharField(required=True, widget=forms.PasswordInput())
class userlogin(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput())
    password=forms.CharField(required=True, widget=forms.PasswordInput())