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
from django.views.generic.base import RedirectView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from simple_email_confirmation.models import EmailAddress
from django.template.loader import render_to_string

class RegistrationFormView(RegistrationView):
	form_class = RegistrationFormAccount
	def form_valid(self, request, form):
		data = form.cleaned_data
		new_user = User.objects.create_user(data['email'], data['email'], data['password1'])
		new_user.confirm_email(new_user.confirmation_key)
		message = render_to_string("account/confirm_email.html", { 'root': request.META['REMOTE_ADDR'], 'user': new_user, })
		send_mail('Email Confirmation', message, settings.EMAIL_HOST_USER, [ data['email']], fail_silently=False)
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

class ConfirmationView(RedirectView):
	permanent = False
	query_string = True

	def get_redirect_url(self, confirmation_key, *args, **kwargs):
		try:
			user = EmailAddress.objects.get(key=confirmation_key).user
			if user.is_confirmed:
				return reverse('account:already_confirmed')
			user.confirm_email(confirmation_key)
			if user.is_confirmed:
				return reverse('account:successfully_confirmed')
			return reverse('note:index')
		except EmailAddress.DoesNotExist:
			return reverse('account:confirmation_key_incorrect')

class ConfirmationKeyIncorrectView(TemplateView):
	template_name = "account/confirmation_key_incorrect.html"

class AlreadyConfirmedView(TemplateView):
	template_name = "account/already_confirmed.html"

class SuccessfullyConfirmedView(TemplateView):
	template_name = "account/successfully_confirmed.html"

		
