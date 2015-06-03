from django.conf.urls import patterns, url
from note.views import IndexView, AddNoteView
from note import views

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note/new/$', AddNoteView.as_view(), name='add_note'),
    url(r'^note/delete/(?P<note_id>\d+)$', views.delete, name='delete_note'),
)