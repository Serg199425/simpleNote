from django.conf.urls import patterns, url
from friends.views import IndexView, AddFriendView, AcceptView, DeleteView


urlpatterns = patterns('',
    url(r'^friends/$', IndexView.as_view(), name='index'),
    url(r'^friends/add_friend$', AddFriendView.as_view(), name='add_friend'),
    url(r'^friends/accept_invintation/(?P<pk>\d+)$', AcceptView.as_view(), name='accept_friend'),
    url(r'^friends/delete/(?P<pk>\d+)$', DeleteView.as_view(), name='delete'),
)