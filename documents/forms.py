# sendemail/forms.py
from django import forms
from documents.models import Document
from django.forms import ModelForm

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'image']

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(DocumentForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = False
        self.fields['image'].required = False
