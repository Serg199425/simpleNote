from django.conf.urls import patterns, url
from account.views import LoginFormView, logout_view, EditView


urlpatterns = patterns('',
    url(r'^account/edit/$', EditView.as_view(), name='edit'),
    url(r'^login/$', LoginFormView.as_view(), name='login_path'),
    url(r'^logout/$', logout_view, name='logout_path'),
)