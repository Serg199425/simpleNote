from django.conf.urls import patterns, url
from groups.views import *

urlpatterns = patterns('',
    url(r'^groups/$', IndexView.as_view(), name='index'),
    url(r'^groups/add$', AddView.as_view(), name='add'),
    url(r'^groups/add_user/(?P<pk>\d+)$', AddUserToGroupView.as_view(), name='add_user'),
    url(r'^groups/accept/(?P<pk>\d+)$', AcceptView.as_view(), name='accept'),
    url(r'^groups/delete/(?P<pk>\d+)$', DeleteView.as_view(), name='delete'),
    url(r'^groups/show_users/(?P<pk>\d+)$', ShowGroupUsersView.as_view(), name='show_users'),
    url(r'^groups/delete_user/(?P<pk>\d+)$', DeleteGroupUserView.as_view(), name='delete_user'),
    url(r'^get_groups_invitations/$', get_groups_invitations),
)