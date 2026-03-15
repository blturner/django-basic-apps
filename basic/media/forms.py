from django import forms

from .models import PhotoSet


class PhotoSetForm(forms.ModelForm):
    class Meta:
        model = PhotoSet
        fields = [
            "title",
            "description",
            "photos",
        ]
        widgets = {
            "photos": forms.CheckboxSelectMultiple,
        }
