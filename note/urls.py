from django.conf.urls import patterns, url
from note.views import *
from note import views

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note/new/$', EditNoteView.as_view(), name='add_note'),
    url(r'^note/show/(?P<pk>\d+)$', ShowView.as_view(), name='show_note'),
    url(r'^note/edit/(?P<pk>\d+)$', EditNoteView.as_view(), name='edit_note'),
    url(r'^note/delete/(?P<pk>\d+)$', DeleteView.as_view(), name='delete_note'),
    url(r'^note/shared/$', SharedNotesView.as_view(), name='shared'),
    url(r'^note/add_to_favorite/(?P<pk>\d+)$', AddFavoriteView.as_view(), name='add_favorite'),
    url(r'^favorites/$', FavoriteIndexView.as_view(), name='favorite_index'),
    url(r'^favorites/remove/(?P<pk>\d+)$', RemoveFavoriteView.as_view(), name='remove_favorite'),
    url(r'^get_shared_notes/$', get_shared_notes),
)