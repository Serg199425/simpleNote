from django.shortcuts import render
from registration.views import RegistrationView
from account.forms import RegistrationFormAccount
from registration.views import ActivationView  

class RegistrationFormView(RegistrationView):
	form_class = RegistrationFormAccount
	def register(request, success_url=None,
         form_class=RegistrationFormAccount, 
         profile_callback=None,
         template_name='registration/registration_form.html',
         extra_context=None):
		super(RegistrationView)
	def get_success_url(self, request, user):
		success_url =  "/register/complete/"
		return success_url
