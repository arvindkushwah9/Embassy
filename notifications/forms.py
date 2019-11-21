# sendemail/forms.py
from django import forms
from notifications.models import Notification
from django.forms import ModelForm

class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['title']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NotificationForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = False
