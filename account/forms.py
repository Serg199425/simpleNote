from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User
from account.models import Account
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.images import get_image_dimensions

class RegistrationFormAccount(RegistrationFormUniqueEmail):
	username = forms.CharField(widget=forms.HiddenInput, required=False)
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Email"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password Confirmation"}))

	def clean_username(self):
		return self.cleaned_data['username']

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).count() > 0:
			raise forms.ValidationError('This email is already in use.')
		return email

	def clean(self):
		if not self.errors:
			localpart = self.cleaned_data['email'].split('@',1)[0][:25]
			c = User.objects.filter(username=localpart).count()
			if c > 0:
				localpart += str(c + 1)
				self.cleaned_data['username'] = localpart
		super(RegistrationFormAccount, self).clean()
		return self.cleaned_data


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Username or Email"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password"}))

class EditForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}))
	avatar = forms.ImageField(required=False)
	class Meta:
		model = Account
	def clean_avatar(self):
		avatar = self.cleaned_data['avatar']
		try:
			main, sub = avatar.content_type.split('/')
			if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
				raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')
            
			if len(avatar) > (20 * 1024):
				raise forms.ValidationError(u'Avatar file size may not exceed 20k.')

		except AttributeError:
			pass
		return avatar
