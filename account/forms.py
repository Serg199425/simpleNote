from django import forms
from registration.forms import RegistrationFormUniqueEmail
from account.models import Account, User
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.images import get_image_dimensions
from django_select2 import AutoModelSelect2MultipleField, NO_ERR_RESP
import operator
from django.db.models import Q
from IPython import embed

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
	def clean_password(self):
		user = User.objects.filter(email=self.cleaned_data['username']).first()
		if not user or not user.check_password(self.cleaned_data['password']):
			raise forms.ValidationError('This email or password is incorrect.')
		return self.cleaned_data['password']

class EditForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"First Name"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Last Name"}))
	class Meta:
		model = Account
		fields = ['first_name', 'last_name']
		
class EditAvatarForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['avatar']


class UserChoices(AutoModelSelect2MultipleField):
	queryset = User.objects
	search_fields = ['email__icontains', ]
	def get_results(self, request, term, page, context):
		try:
			query_email = reduce(operator.or_, (Q(email__icontains = word) for word in term.split()))
			query_first_name = reduce(operator.or_, (Q(account__first_name__icontains = word) for word in term.split()))
			query_last_name = reduce(operator.or_, (Q(account__last_name__icontains = word) for word in term.split()))
			results = User.objects.filter(query_first_name | query_last_name | query_email).exclude(id=request.user.id)[:5]
			results = [(u.id, u.email + ' ' + u.account.first_name + ' ' + u.account.last_name) for u in results]
			return NO_ERR_RESP, False, results
		except:
			results = []
			return NO_ERR_RESP, False, results