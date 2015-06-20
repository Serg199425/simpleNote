from django.conf.urls import *

urlpatterns = patterns('autocomplete_tags.views',
    url(r'^list$', 'list_tags', name='tagging_autocomplete_tagit-list'),
)
