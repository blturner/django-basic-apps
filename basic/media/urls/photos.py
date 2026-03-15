from django.views.generic import CreateView, DetailView, ListView
from django.urls import path

from basic.media.models import Photo, PhotoSet
from ..forms import PhotoSetForm


class PhotoList(ListView):
    queryset = Photo.objects.all()


class PhotoSetList(ListView):
    queryset = PhotoSet.objects.all()


class PhotoDetail(DetailView):
    queryset = Photo.objects.all()


class PhotoSetDetail(DetailView):
    queryset = PhotoSet.objects.all()


class PhotoSetCreate(CreateView):
    model = PhotoSet
    form_class = PhotoSetForm


urlpatterns = [
    path("sets/create/", PhotoSetCreate.as_view(), name="photo_set_create"),
    path(
        "sets/<slug:slug>/", PhotoSetDetail.as_view(), name="photo_set_detail"
    ),
    path("sets/", PhotoSetList.as_view(), name="photo_set_list"),
    path("<slug:slug>/", PhotoDetail.as_view(), name="photo_detail"),
    path("", PhotoList.as_view(), name="photo_list"),
]
