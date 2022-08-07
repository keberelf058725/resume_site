from django.forms import ModelForm
from django import forms
from .models import CV_Letter_Data
from django.db.models.fields import BLANK_CHOICE_DASH

link_choices = [('Indeed', 'Indeed'), ('Reference', 'Reference'), ('Direct Apply', 'Direct Apply'),('LinkedIN', 'LinkedIN')]
field_type_choices = [('Yes', 'Yes'), ('No', 'No')]
job_type_choices = [('Data Analyst', 'Data Analyst'), ('Programing', 'Programing'),
                    ('Software Analyst', 'Software Analyst'), ('Other', 'Other')]

email_choices = [('Zoom', 'Zoom'), ('Phone', 'Phone')]


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class CV_Letter_Form(ModelForm):
    Name = forms.CharField(max_length=255)
    link = forms.CharField(label='How did you find my resume? ',
                           widget=forms.Select(choices=BLANK_CHOICE_DASH + link_choices))
    Job_type = forms.CharField(label='Did I apply to a healthcare company? ',
                               widget=forms.Select(choices=BLANK_CHOICE_DASH + field_type_choices))
    Field_Applied = forms.CharField(label='What position did I apply to? ',
                                    widget=forms.Select(choices=BLANK_CHOICE_DASH + job_type_choices))

    class Meta:
        model = CV_Letter_Data
        fields = ['Name', 'link', 'Job_type', 'Field_Applied']


class email_form(forms.Form):
    Name = forms.CharField(max_length=255, label='Your Name')
    Email = forms.EmailField(max_length=255, label='Your Email')
    Meeting_type = forms.CharField(label='What would be best Zoom or Phone? ',
                                   widget=forms.Select(choices=BLANK_CHOICE_DASH + email_choices))
    Time = forms.TimeField(label='What would be the best time for me to schedule Zoom or be ready for a call?',widget=TimePickerInput)
    Date = forms.DateField(label='What would be the best date for me to schedule Zoom or be ready for a call?', widget=DatePickerInput)
