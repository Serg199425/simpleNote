from django.conf.urls import include, url
from django.contrib import admin
from account.views import RegistrationFormView, LoginFormView, RegistrationCompleteView
from django.conf import settings

urlpatterns = [
	url(r'^register/$', RegistrationFormView.as_view(), name='registration_register'),
	url(r'^register/complete/$', RegistrationCompleteView.as_view(), name='registration_complete'),
	url(r'^', include('account.urls', namespace="account")),
	url(r'^', include('note.urls', namespace="note")),
    url(r'^', include('friends.urls', namespace="friends")),
    url(r'^', include('groups.urls', namespace="groups")),
    url(r'^', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('content_pages.urls', namespace="content_pages")),
]