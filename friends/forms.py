from django import forms
from django.contrib.auth.models import User
from IPython import embed

class AddFriendForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control small-input','placeholder':"Email"}))
