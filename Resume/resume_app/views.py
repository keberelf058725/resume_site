from django.shortcuts import render, redirect
from .forms import CV_Letter_Form


# Create your views here.


def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CV_Letter_Form(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'cv.html', {})

    else:
        form = CV_Letter_Form()

    return render(request, "home.html", {'form': form})


def cover_letter_view(request, *args, **kwargs):
    return render(request, "cv.html", {})
