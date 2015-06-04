from django.conf.urls import patterns, url
from note.views import IndexView, EditNoteView
from note import views

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note/new/$', EditNoteView.as_view(), name='add_note'),
    url(r'^note/edit/(?P<note_id>\d+)$', EditNoteView.as_view(), name='add_note'),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete, name='delete_note'),
)