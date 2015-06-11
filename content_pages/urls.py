from django.conf.urls import patterns, url
from content_pages.views import AboutUsView


urlpatterns = patterns('',
    url(r'^about_us/$', AboutUsView.as_view(), name='about_us'),
)