from django import forms

from mailing.models import Client
from services import StileFormMixin


class ClientForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
