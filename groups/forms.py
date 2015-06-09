from django import forms
from django.contrib.auth.models import User

class AddGroupForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Name"}))

class AddUserToGroupForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Email"}))
