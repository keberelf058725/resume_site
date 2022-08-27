from django.shortcuts import render, redirect
from .forms import CV_Letter_Form, email_form
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime
import os
import mimetypes
from django.http import HttpResponse
from .graph import ammount_trained
# Create your views here.

def power_bi_view(request, *args, **kwargs):
    return render(request, "pbi.html", {})


def software_an_view(request, *args, **kwargs):
    if request.method == 'GET':

        context = {}

        context['trained_chart'] = ammount_trained()

    return render(request, "sftwr_analysis.html", context)

def home_view(request, *args, **kwargs):
    if request.method == 'GET':

        context = {}

        context['trained_chart'] = ammount_trained()

    return render(request, "home.html", context)

def cover_letter_customize_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CV_Letter_Form(request.POST)
        if form.is_valid():
            form.save()

            Name = form.cleaned_data['Name']
            link = form.cleaned_data['link']
            Job_type = form.cleaned_data['Job_type']
            Field_Applied = form.cleaned_data['Field_Applied']

            send_mail(Name + ' Filled out the Cover Letter Form',Name + ' - ' + link + ' - ' + Job_type + ' - ' + Field_Applied,
                      'myresumeonlinekcjr@gmail.com', ['kcaldonjr@gmail.com', 'myresumeonlinekcjr@gmail.com'])

            #selection for all healthcare jobs
            if 'Yes' in Job_type:

                context = {'Name': Name, 'link': link, 'Job_type':Job_type, 'Field_Applied': Field_Applied}

                return render(request, 'cv_bh_sa.html', context)
            #selections for software but no healthcare
            if 'No' in Job_type and 'Software Analyst' in Field_Applied:

                context = {'Name': Name, 'link': link, 'Job_type': Job_type, 'Field_Applied': Field_Applied}

                return render(request, 'cv_bh_sa.html', context)

            # selections for Data Analyst only
            if 'No' in Job_type and 'Data Analyst' in Field_Applied:
                context = {'Name': Name, 'link': link, 'Job_type': Job_type, 'Field_Applied': Field_Applied}

                return render(request, 'cv_da.html', context)
            # selection for Programing only
            if 'No' in Job_type and 'Programing' in Field_Applied:
                context = {'Name': Name, 'link': link, 'Job_type': Job_type, 'Field_Applied': Field_Applied}

                return render(request, 'cv_op.html', context)

            else:
                context = {'Name': Name, 'link': link, 'Job_type': Job_type, 'Field_Applied': Field_Applied}

                return render(request, 'cv_bh_sa.html', context)

        else:
            messages.error(request, 'Unknown Error: Operation Cancelled')

    else:
        form = CV_Letter_Form()

    return render(request, "cover_letter_customize.html", {'form': form})


def cv_bh_sa_view(request, *args, **kwargs):
    return render(request, "cv_bh_sa.html", {})

def cv_op_view(request, *args, **kwargs):
    return render(request, "cv_op.html", {})

def cv_da_view(request, *args, **kwargs):
    return render(request, "cv_da.html", {})

def jobhx_view(request, *args, **kwargs):
    return render(request, "jobhx.html", {})

def school_view(request, *args, **kwargs):
    return render(request, "School.html", {})

def ref_view(request, *args, **kwargs):
    return render(request, "references.html", {})

def skills_view(request, *args, **kwargs):
    return render(request, "skills.html", {})

def call_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = email_form(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Meeting_type = form.cleaned_data['Meeting_type']
            Time = form.cleaned_data['Time']
            Date = form.cleaned_data['Date']
            Time = Time.strftime("%I:%M %p")
            Date = str(Date)
            Date = datetime.strptime(Date, "%Y-%m-%d").strftime("%m/%d/%Y")
            Time = str(Time)

            if 'Zoom' in Meeting_type:
                html = render_to_string('zoom_response.html',
                                        {'Name': Name,
                                         'Email': Email,
                                         'Meeting_type': Meeting_type,
                                         'Time': Time,
                                         'Date': Date}
                                        )

                send_mail(Name + ' - ' + Meeting_type,'Form user is requesting a meeting at ' + Time + ' on ' + Date + ' their email is: ' + Email, 'myresumeonlinekcjr@gmail.com', ['kcaldonjr@gmail.com','myresumeonlinekcjr@gmail.com'])

                send_mail(Name + ' - ' + Meeting_type, 'Meeting Details:',
                          'myresumeonlinekcjr@gmail.com', [Email], html_message=html)

            if 'Phone' in Meeting_type:
                html = render_to_string('phone_response.html',
                                        {'Name': Name,
                                         'Email': Email,
                                         'Meeting_type': Meeting_type,
                                         'Time': Time,
                                         'Date': Date})

                send_mail(Name + ' - ' + Meeting_type,'Form user is requesting a meeting at ' + Time + ' on ' + Date + ' their email is: ' + Email, 'myresumeonlinekcjr@gmail.com', ['kcaldonjr@gmail.com','myresumeonlinekcjr@gmail.com'])

                send_mail(Name + ' - ' + Meeting_type, 'Meeting Details:',
                          'myresumeonlinekcjr@gmail.com', [Email], html_message=html)

            return redirect('home')


    else:
        form = email_form()

    return render(request, "call.html", {'form': form})

def dl_resume_view(request, *args, **kwargs):
    if request.method == 'GET':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/static/Kevin Caldon - Resume.pdf'
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % 'Kevin Caldon - Resume.pdf'
        return response
    else:
        pass
    return redirect('home')
