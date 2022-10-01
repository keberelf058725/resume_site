"""Resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resume_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover_letter_customize', views.cover_letter_customize_view, name='cover_letter_customize'),
    path('hc_sw', views.cv_bh_sa_view, name='hc_sw'),
    path('o_p', views.cv_op_view, name='o_p'),
    path('o_da', views.cv_da_view, name='o_da'),
    path('jobhx', views.jobhx_view, name='jobhx'),
    path('pbi', views.power_bi_view, name='pbi'),
    path('pbi_embedded', views.pbi_embedded_view, name='pbi_embedded'),
    path('school', views.school_view, name='school'),
    path('references', views.ref_view, name='references'),
    path('sft', views.software_an_view, name='sft'),
    path('skills', views.skills_view, name='skills'),
    path('call', views.call_view, name='call'),
    path('about_me', views.about_view, name='about_me'),
    path('dl_resume', views.dl_resume_view, name='dl_resume'),
    path('', views.home_view, name='home'),
]
