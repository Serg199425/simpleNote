from django.shortcuts import render
from registration.views import RegistrationView
from account.forms import RegistrationFormAccount, LoginForm, EditForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from account.models import Account

class RegistrationFormView(RegistrationView):
	form_class = RegistrationFormAccount

	def form_valid(self, request, form):
		email = request.REQUEST.get('email', None)
		password = request.REQUEST.get('password1', None)
		new_user = User.objects.create_user(email, email, password)
		new_user = auth.authenticate(username = new_user.username, password = password)
		if new_user is not None:
			account = Account(user=new_user, first_name="", last_name="")
			account.save()
			auth.login(request, new_user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/login')

	def get_success_url(self, request, user):
		success_url = reverse('registration_complete')
		return success_url


class RegistrationCompleteView(TemplateView):
	template_name = "registration/registration_complete.html"
		

class LoginFormView(FormView):
	template_name = "registration/login_form.html"
	form_class = LoginForm
	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		try:
			user = User.objects.get(email=username)
		except User.DoesNotExist:
			return None
		if user.check_password(password):
			user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(self.request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect(reverse('account:login_path'))

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

		
