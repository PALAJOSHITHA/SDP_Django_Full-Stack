"""EPCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from EBS2021.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name="index"),
    path('Login', Login ,name="Login"),
    path('about', about ,name="about"),
    path('feedback', feedback_view, name='feedback'),
    path('add_Aerospace', add_Aerospace ,name="add_Aerospace"),
    path('view_employee', view_employee ,name="view_employee"),
    path('home3', home3 ,name="home3"),
    path('add_Healthcare', add_Healthcare ,name="add_Healthcare"),
    path('add_Education', add_Education ,name="add_Education"),
    path('add_Development', add_Development ,name="add_Development"),
    path('add_RealEstate', add_RealEstate ,name="add_RealEstate"),
    path('add_Resume', add_Resume ,name="add_Resume"),
    path('full_time', full_time ,name="full_time"),
    path('part_time', part_time ,name="part_time"),
    path('resume_success', resume_success ,name="resume_success"),
    path('contact', contact ,name="contact"),
    path('innerhome', innerhome ,name="innerhome"),
    path('user_Home', user_Home ,name="user_Home"),
    path('Logout', Logout ,name="Logout"),
    path('usersignup', usersignup ,name="usersignup"),
    path('adminsignup',usersignup, name="adminsignup"),
    path('adminhome',adminhome, name="adminhome"),
    path('Userlogin', Userlogin ,name="Userlogin"),
    path('userhome', userhome ,name="userhome"),
    path('RecruiterSignup',RecruiterSignup,name='RecruiterSignup'),
    path('Recruiterlogin',Recruiterlogin, name="Recruiterlogin"),
     path('Recruiterhome', Recruiterhome, name="Recruiterhome"),
    path('add_category', add_category,name="add_category"),
    path('view_category', view_category ,name="view_category"),
    path('delete_category(?p<int:pid>)', delete_category ,name="delete_category"),
    path('view_user', view_user ,name="view_user"),
    path('delete_user(?p<int:pid>)', delete_user ,name="delete_user"),
    path('book_now/<int:pid>', book_now ,name="book_now"),
    path('change_passworduser', change_passworduser ,name="change_passworduser"),
    path('change_passwordadmin', change_passwordadmin ,name="change_passwordadmin"),
    path('booking_request', booking_request ,name="booking_request"),
    path('accepted_booking',accepted_booking ,name="accepted_booking"),
    path('rejected_booking',rejected_booking ,name="rejected_booking"),
    path('all_booking',all_booking ,name="all_booking"),
    path('confirmed_booking',confirmed_booking ,name="confirmed_booking"),

    path('payment/<int:pid>',payment,name="payment"),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
