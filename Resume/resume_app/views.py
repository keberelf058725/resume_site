from django.shortcuts import render, redirect
from .forms import CV_Letter_Form


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def cover_letter_customize_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CV_Letter_Form(request.POST)
        if form.is_valid():
            form.save()

            Name = request.POST['Name']
            link = request.POST['link']
            Job_type = request.POST['Job_type']
            Field_Applied = request.POST['Field_Applied']

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
    return render(request, "call.html", {})