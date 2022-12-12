from django import forms
from django.forms import ModelForm, DateInput, Textarea
from .models import Engineer, Site, AssetRequest


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('name', 'sudo_name')


class RequestForm(ModelForm):
    class Meta:
        model = AssetRequest
        fields = '__all__'