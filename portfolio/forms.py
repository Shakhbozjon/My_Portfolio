from django import forms
from .models import ContactMe


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'message')