from django.views.generic import DetailView, ListView
from django.urls import path

from basic.media.models import Audio


urlpatterns = [
    path("<slug:slug>/", DetailView.as_view(queryset=Audio.objects.all())),
    path("", ListView.as_view(queryset=Audio.objects.all())),
]
