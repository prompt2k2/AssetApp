from django import forms

office = [('Operations','Operations'),('OHSE','OHSE'), 
          ('Admin','Admin'),('IT','IT')]

RM = [()]

class IMRegisterForms(forms.Form):
    
    name = forms.CharField(max_length=80)
    job_role = forms.CharField(max_length=30)
    incident_type= forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=office)
    incident_date = forms.DateField()
    incident_time = forms.DateTimeField()
    person_involved = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    incident_description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    witness = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    loss = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    reported_to = forms.CharField(max_length=80)
    date_reported = forms.DateField()
    report_method = forms.ChoiceField()
    actions = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    