from django.conf.urls import include, url
from django.contrib import admin
from account.views import RegistrationFormView, LoginFormView, RegistrationCompleteView

urlpatterns = [
	url(r'^register/$', RegistrationFormView.as_view(), name='registration_register'),
	url(r'^register/complete/$', RegistrationCompleteView.as_view(), name='registration_complete'),
	url(r'^', include('account.urls', namespace="account")),
    url(r'^', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
]
