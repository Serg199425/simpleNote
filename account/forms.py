from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User

class RegistrationFormAccount(RegistrationFormUniqueEmail):
	username = forms.CharField(widget=forms.HiddenInput, required=False)
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Email"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password Confirmation"}))

	def clean_username(self):
		return self.cleaned_data['username']

	def clean(self):
		if not self.errors:
			localpart = self.cleaned_data['email'].split('@',1)[0][:25]
			c = User.objects.filter(username=localpart).count()
			if c > 0:
				localpart += str(c + 1)
				self.cleaned_data['username'] = localpart
		super(RegistrationFormAccount, self).clean()
		return self.cleaned_data