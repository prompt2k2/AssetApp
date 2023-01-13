from django import forms
from django.forms import ModelForm, DateInput, Textarea, TextInput, NumberInput
from .models import Engineer, Site, AssetRequest


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = '__all__' #('site_id', 'name', 'sudo_name')


class RequestForm(ModelForm):
    class Meta:
        model = AssetRequest
        fields = '__all__'
        widgets = {

            
            'manufacturer': TextInput(),
            'bad_last_service': DateInput(attrs = {'type':'date'}),
            'bad_serial_number': TextInput(),
            'bad_model_number': TextInput(),
            'bad_equipment_name': TextInput(),
            'bad_equipment_rating': TextInput(),
            'bad_days_in_ops': NumberInput(),
            'bad_installation_date': DateInput(attrs = {'type':'date'}),

            'new_equipment_name': TextInput(),
            'new_manufacturer': TextInput(),
            'new_equipment_rating': TextInput(),
            'expected_date': DateInput(attrs = {'type':'date'}),

            'sitemanager_comment': Textarea(attrs = {'rows':2, 'placeholder':'HOD comment'}),
            'hod_comment': Textarea(attrs = {'rows':2, 'placeholder':'HOD comment'}),

            'justification': Textarea(attrs = {'rows':3, 'placeholder':'Please describe the justification for replacement'}),
            }
        
    
