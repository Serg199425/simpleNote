from django.conf.urls import patterns, url
from account.views import *


urlpatterns = patterns('',
    url(r'^account/edit/$', EditView.as_view(), name='edit'),
    url(r'^login/$', LoginFormView.as_view(), name='login_path'),
    url(r'^logout/$', logout_view, name='logout_path'),
    url(r'^account/confirm/(?P<confirmation_key>[a-zA-Z0-9]+)$', ConfirmationView.as_view(), name='confirm'),
    url(r'^confirmation_key_incorrect/$', ConfirmationKeyIncorrectView.as_view(), name='confirmation_key_incorrect'),
	url(r'^already_confirmed/$', AlreadyConfirmedView.as_view(), name='already_confirmed'),
	url(r'^successfully_confirmed/$', SuccessfullyConfirmedView.as_view(), name='successfully_confirmed'),
)