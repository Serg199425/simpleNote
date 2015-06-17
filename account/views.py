from django.shortcuts import render
from registration.views import RegistrationView
from account.forms import RegistrationFormAccount, LoginForm, EditForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from account.models import Account, User
from django.contrib.auth.decorators import login_required
from privateviews.decorators import login_not_required
from django.core.mail import EmailMessage


class RegistrationFormView(RegistrationView):
	form_class = RegistrationFormAccount
	def form_valid(self, request, form):
		data = form.cleaned_data
		new_user = User.objects.create_user(data['email'], data['email'], data['password1'])
		new_user.confirm_email(new_user.confirmation_key)
		EmailMessage('Email Confirmation', 'Use %s to confirm your email' % new_user.confirmation_key, "aaa@gmail.com", [data['email']])
		Account(user=new_user, first_name="", last_name="").save()
		return HttpResponseRedirect(reverse('registration_complete'))

class RegistrationCompleteView(TemplateView):
	template_name = "registration/registration_complete.html"
		

class LoginFormView(FormView):
	template_name = "registration/login_form.html"
	form_class = LoginForm
	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		auth.login(self.request, auth.authenticate(username = username, password = password))
		return HttpResponseRedirect('/')

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect(reverse('account:login_path'))

class EditView(FormView):
	form_class = EditForm
	template_name = "account/edit_form.html"
	def get_initial(self):
		user = self.request.user
		account = Account.objects.get(user_id=user.id)
		return {'first_name': account.first_name, 'last_name': account.last_name, 'avatar': account.avatar }
	def form_valid(self, form):
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		avatar = form.cleaned_data['avatar']
		user = self.request.user
		try:
			account = Account.objects.get(user_id=user.id)
			account.first_name = first_name
			account.last_name = last_name
			account.avatar = avatar
			account.save()
			return HttpResponseRedirect(reverse('account:edit'))
		except Account.DoesNotExist:
			return HttpResponseRedirect('/')

		
