from django.conf.urls import patterns, url
from note.views import IndexView, EditNoteView, ShowView, DeleteView
from note import views

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note/new/$', EditNoteView.as_view(), name='add_note'),
    url(r'^note/show/(?P<pk>\d+)$', ShowView.as_view(), name='show_note'),
    url(r'^note/edit/(?P<pk>\d+)$', EditNoteView.as_view(), name='edit_note'),
    url(r'^note/delete/(?P<pk>\d+)$', DeleteView.as_view(), name='delete_note'),
)