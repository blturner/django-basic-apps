from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from basic.media.models import Photo, PhotoSet


urlpatterns = patterns('',
    url(r'^sets/(?P<slug>[-\w]+)/$', DetailView.as_view(model=PhotoSet), name='photo_set_detail'),
    url(r'^sets/$', ListView.as_view(model=PhotoSet), name='photo_set_list'),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(model=Photo), name='photo_detail'),
    url(r'^$', ListView.as_view(model=Photo), name='photo_list'),
)
