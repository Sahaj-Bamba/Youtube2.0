import django
from django import forms
from django.forms import HiddenInput

from .models import video, videoOrg
from .models import tag


class videoForm(forms.ModelForm):
    class Meta:
        model = videoOrg
        fields = ["videofile"]


class videoData(forms.ModelForm):
    class Meta:
        model = video
        fields = ["name", "description"]

# class videoForm(forms.ModelForm):
#     class Meta:
#         model = video
#         fields = ["name", "videofile", "tags"]
#
#         tags = forms.ModelMultipleChoiceField(queryset=tag.objects.all())
#
#         # Overriding __init__ here allows us to provide initial
#         # data for 'toppings' field
#         def __init__(self, *args, **kwargs):
#
#             self.fields['owner'].widgets = HiddenInput()
#
#             # Only in case we build the form from an instance
#             if kwargs.get('instance'):
#                 # We get the 'initial' keyword argument or initialize it
#                 # as a dict if it didn't exist.
#                 initial = kwargs.setdefault('initial', {})
#                 # The widget for a ModelMultipleChoiceField expects
#                 # a list of primary key for the selected data.
#                 initial['tags'] = [t.pk for t in kwargs['instance'].topping_set.all()]
#
#             forms.ModelForm.__init__(self, *args, **kwargs)
#
#         # Overriding save allows us to process the value of 'tags' field
#         def save(self, commit=True):
#             # Get the unsave Video instance
#             instance = forms.ModelForm.save(self, False)
#
#             # Prepare a 'save_m2m' method for the form,
#             old_save_m2m = self.save_m2m
#
#             def save_m2m():
#                 old_save_m2m()
#                 # This is where we actually link the pizza with toppings
#                 instance.tags_set.clear()
#                 instance.tags_set.add(*self.cleaned_data['tags'])
#
#             self.save_m2m = save_m2m
#
#             # Do we need to save all changes now?
#             if commit:
#                 instance.save()
#                 self.save_m2m()
#
#             return instance