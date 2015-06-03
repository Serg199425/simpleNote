from registration.signals import user_registered, user_activated
from django.contrib import auth

def login_on_activation(sender, user, request, **kwargs):
	user.backend='django.contrib.auth.backends.ModelBackend' 
	auth.login(request,user)

	user_activated.connect(login_on_activation)
	user_registered.connect(user_created)