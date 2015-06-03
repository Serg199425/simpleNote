from django.conf.urls import include, url
from django.contrib import admin
from account.views import RegistrationFormView

urlpatterns = [
	url(r'^register/$', RegistrationFormView.as_view(), name='registration_register'),
    url(r'^', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
]
