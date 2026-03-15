from django.views.generic import DetailView, ListView
from django.urls import path

from basic.media.models import Video, VideoSet


video_qs = Video.objects.all()
videoset_qs = VideoSet.objects.all()


urlpatterns = [
    path(
        "sets/<slug:slug>/",
        DetailView.as_view(queryset=videoset_qs),
        name="video_set_detail",
    ),
    path(
        "sets/",
        ListView.as_view(queryset=videoset_qs),
        name="video_set_detail",
    ),
    path(
        "<slug:slug>/",
        DetailView.as_view(queryset=video_qs),
        name="video_detail",
    ),
    path("", ListView.as_view(queryset=video_qs), name="video_list"),
]
