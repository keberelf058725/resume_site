from django.forms import ModelForm
from django import forms
from .models import CV_Letter_Data

link_choices = [('Please Choose','Please Choose'),('Indeed','Indeed'), ('Reference','Reference'), ('Direct Apply','Direct Apply')]
field_type_choices = [('Please Choose','Please Choose'),('Healthcare','Healthcare'), ('Behavioral Healthcare', 'Behavioral Healthcare'),('Programing','Programing'), ('Data Science','Data Science')]
job_type_choices = [('Please Choose','Please Choose'),('Data Analyst', 'Data Analyst'),('Programing','Programing'), ('Software Analyst','Software Analyst')]

class CV_Letter_Form(ModelForm):
    Name = forms.CharField(max_length=255)
    link = forms.CharField(label='How did you find my resume? ', widget=forms.Select(choices=link_choices))
    Job_type = forms.CharField(label='What field do you work in? ', widget=forms.Select(choices=field_type_choices))
    Field_Applied = forms.CharField(label='What job did I apply to? ', widget=forms.Select(choices=job_type_choices))
    class Meta:
        model = CV_Letter_Data
        fields = ['Name', 'link', 'Job_type', 'Field_Applied']