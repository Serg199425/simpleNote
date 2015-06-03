from django.shortcuts import render
from registration.views import RegistrationView
from account.forms import RegistrationFormAccount, LoginForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from IPython import embed
from django.contrib import auth
from django.http import HttpResponseRedirect

class RegistrationFormView(RegistrationView):
	form_class = RegistrationFormAccount
	def register(self, request, success_url=None,
         form_class=RegistrationFormAccount, 
         profile_callback=None,
         template_name='registration/registration_form.html',
         extra_context=None):
		userMail = request.REQUEST.get('email', None)
		userPass = request.REQUEST.get('password', None)

	def form_valid(self, request, form):
		email = request.REQUEST.get('email', None)
		password = request.REQUEST.get('password1', None)
		new_user = User.objects.create_user(email, email, password)

		if new_user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/login')

	def get_success_url(self, request, user):
		success_url = reverse('registration_complete')
		return success_url


class RegistrationCompleteView(TemplateView):
	template_name = "registration/registration_complete.html"
		

class LoginFormView(FormView):
	template_name = "registration/login.html"
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
			return HttpResponseRedirect('/login')

class IndexView(TemplateView):
	template_name = "account/index.html"
