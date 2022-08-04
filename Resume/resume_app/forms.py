from django.forms import ModelForm
from django import forms
from .models import CV_Letter_Data
from django.db.models.fields import BLANK_CHOICE_DASH

link_choices = [('Indeed','Indeed'), ('Reference','Reference'), ('Direct Apply','Direct Apply')]
field_type_choices = [('Yes','Yes'), ('No','No')]
job_type_choices = [('Data Analyst', 'Data Analyst'),('Programing','Programing'), ('Software Analyst','Software Analyst'), ('Other','Other')]

class CV_Letter_Form(ModelForm):
    Name = forms.CharField(max_length=255)
    link = forms.CharField(label='How did you find my resume? ', widget=forms.Select(choices=BLANK_CHOICE_DASH + link_choices))
    Job_type = forms.CharField(label='Did I apply to a healthcare company? ', widget=forms.Select(choices=BLANK_CHOICE_DASH + field_type_choices))
    Field_Applied = forms.CharField(label='What position did I apply to? ', widget=forms.Select(choices=BLANK_CHOICE_DASH + job_type_choices))
    class Meta:
        model = CV_Letter_Data
        fields = ['Name', 'link', 'Job_type', 'Field_Applied']