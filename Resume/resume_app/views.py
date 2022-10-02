from django.shortcuts import render, redirect
from .forms import contact_form
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime
import os
import mimetypes
from django.http import HttpResponse



# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def call_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Message = form.cleaned_data['Message']

            html = render_to_string('zoom_response.html',
                                    {'Name': Name,
                                     'Email': Email,
                                     'Message': Message, }
                                    )

            send_mail(Name + ' - is requesting a meeting','Their message is: ' + Message + '. ' + 'Their email is: ' + Email, 'myresumeonlinekcjr@gmail.com',
                      ['kcaldonjr@gmail.com', 'myresumeonlinekcjr@gmail.com'])

            send_mail(Name, 'Contact Details:',
                      'myresumeonlinekcjr@gmail.com', [Email], html_message=html)

            return redirect('home')


    else:
        form = contact_form()

    return render(request, "call.html", {'form': form})

def pbi_embedded_view(request, *args, **kwargs):
    return render(request, "PBI_interactive.html", {})

def report_list_view(request, *args, **kwargs):
    return render(request, "report_list.html", {})



