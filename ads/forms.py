# sendemail/forms.py
from django import forms
from ads.models import Ad
from django.forms import ModelForm

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(AdForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = False
