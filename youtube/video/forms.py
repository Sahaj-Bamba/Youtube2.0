from django.contrib.contenttypes import forms

from .models import video


class videoForm(forms.ModelForm):
    class Meta:
        model = video
        fields = ["name", "videofile", "owner", "tags"]
