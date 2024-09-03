from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserSignup,RecruiterRegistration
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Feedback from {}'.format(name)
            message = 'From: {} <{}>\n\n{}'.format(name, email, message)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_RECEIVER], fail_silently=False)
            return render(request, 'thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def index(request):
    return render(request ,"index.html")

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            try:
                if user.is_authenticated:
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"                   
    d = {'error':error}
    return render(request,"Login.html",d)

def Userlogin(request):
    error=""
    if request.method=='POST':
        e=request.POST['email']
        p=request.POST['pwd']
        user=authenticate(username=e,password=p)
        if user:
            try:
                user1 = UserSignup.objects.get(user=user)
                if user1:
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"                    
    d = {'error':error}
    return render(request,'userlogin.html',d)    

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""    
    if request.method=="POST":
        c= request.POST['currentpassword']
        n= request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
               u.set_password(n) 
               u.save()
               error="no"
            else:
               error="not"   
        except:
            error="yes"    
    d={"error":error}   
    return render(request,"changepassworduser.html",d) 

def userhome(request):
    if not request.user.is_authenticated:
        return redirect('Userlogin')
    user = request.user 
    data = UserSignup.objects.get(user=user)
    error=""
    if request.method=='POST':
        con=request.POST['contact']
        fn=request.POST['fname']
        ln=request.POST['lname']
        address = request.POST['address']
        data.mobile = con
        data.user.first_name = fn
        data.user.last_name = ln
        data.address = address
        try:
            data.save()
            data.user.save()
            error="no"
        except:
            error="yes" 
        try:
            i=request.FILES['image']
            data.image = i
            data.save()
            error="no"
        except:
            pass
    d ={"data":data,'error':error}   
    return render(request ,"userhome.html",d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error=""    
    if request.method=="POST":
        c= request.POST['currentpassword']
        n= request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
               u.set_password(n) 
               u.save()
               error="no"
            else:
               error="not"   
        except:
            error="yes"    
    d={"error":error}   
    return render(request,"changepassword_admin.html",d)

def add_category(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    if request.method=='POST':
        cn=request.POST['cname']
        try:
           Category.objects.create(categoryname=cn)
           error="no"
        except:
            error="yes"
    d = {'error':error}    
    return render(request ,"add_category.html",d)

def view_category(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    cat = Category.objects.all()
    d = {'cat':cat}    
    return render(request ,"view_category.html",d) 

def delete_category(request,pid):
      if not request.user.is_authenticated:
        return redirect('Login')
      apoint= Category.objects.get(id=pid)
      apoint.delete()
      return redirect('view_category')

def view_user(request):

    user1 = UserSignup.objects.all()
    d = {'user1':user1}    
    return render(request ,"view_user.html",d)

def delete_user(request,pid):
      if not request.user.is_authenticated:
        return redirect('Login')
      apoint= UserSignup.objects.get(id=pid)
      apoint.delete()
      return redirect('view_user')

def about(request):
    return render(request ,"about.html")
def add_Aerospace(request):
    return render(request ,"add_Aerospace.html")
def add_Healthcare(request):
    return render(request ,"add_Healthcare.html")
def add_Education(request):
    return render(request ,"add_Education.html")
def add_Development(request):
    return render(request ,"add_Development.html")
def add_RealEstate(request):
    return render(request ,"add_realEstate.html")
def full_time(request):
    return render(request ,"full_time.html")
def part_time(request):
    return render(request ,"part_time.html")
def resume_success(request):
    return render(request ,"resume_success.html")
def user_Home(request):
    return render(request ,"user_Home.html")
def adminhome(request):
    return render(request ,"adminhome.html")
def home3(request):
    return render(request ,"home3.html")

def add_Resume(request):
    error=""
    if request.method=='POST':
        fn=request.POST['fname']
        ln = request.POST['lname']
        pas=request.POST['pwd']
        em=request.POST['email']
        con=request.POST['contact']
        address = request.POST['address']
        i=request.FILES['image']

        try:
            user = User.objects.create_user(username=em,password=pas,first_name=fn,last_name=ln)
            UserSignup.objects.create(user=user,mobile=con,image=i,address=address)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_Resume.html',d)
def usersignup(request):
    error=""
    if request.method=='POST':
        fn=request.POST['fname']
        ln = request.POST['lname']
        pas=request.POST['pwd']
        em=request.POST['email']
        con=request.POST['contact']
        address = request.POST['address']
        i=request.FILES['image']

        try:
            user = User.objects.create_user(username=em,password=pas,first_name=fn,last_name=ln)
            UserSignup.objects.create(user=user,mobile=con,image=i,address=address)
            error="no"
        except:
            error="yes" 
    d = {'error':error}        
    return render(request,'usersignup.html',d)
def adminsignup(request):
    return render(request, "adminsignup.html")
def Logout(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    logout(request)
    return render(request,"index.html")

def book_now(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    event1=Job.objects.get(id=pid)
    user = request.user
    userinfo = UserSignup.objects.get(user=user)
    if request.method=='POST':
        p=request.POST['person']
        t=request.POST['total']
        try:
           Booking.objects.create(userinfo = userinfo,eventinfo=event1,person=p,total=t,status="pending",bookingdate=date.today())
           error="no"
        except:
           error="yes"
    d = {'event1':event1,'error':error}
    return render(request ,"book_now.html",d)

def booking_request(request):
    b = Booking.objects.filter(status="pending")
    return render(request ,"booking_request.html",locals())
def accepted_booking(request):
    b = Booking.objects.filter(status="Accept(Not Paid)")
    return render(request ,"accepted_booking.html",locals())

def rejected_booking(request):
    b = Booking.objects.filter(status="Reject")
    return render(request ,"rejected_booking.html",locals())
def all_booking(request):
    b = Booking.objects.all()
    return render(request ,"all_booking.html",locals())

def confirmed_booking(request):
    b = Booking.objects.filter(status="Confirmed(Paid)")
    return render(request ,"confirmed_booking.html",locals())
def contact(request):
    return render(request ,"contact.html")
def innerhome(request):
    return render(request ,"innerhome.html")
def payment(request,pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    booking = Booking.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        cardnumber = request.POST['cardnumber']
        cardex = request.POST['cardex']
        cvv = request.POST['cvv']
        try:
            booking.cardno = cardnumber
            booking.expirydate = cardex
            booking.cvv = cvv
            booking.status = "Confirmed(Paid)"
            booking.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'payment.html', locals())

def RecruiterSignup(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        pas = request.POST['pwd']
        em = request.POST['email']
        con = request.POST['contact']
        address = request.POST['address']
        i = request.FILES['image']
        try:
            recruiter = User.objects.create_user(username=em, password=pas, first_name=fn, last_name=ln)
            UserSignup.objects.create(user=recruiter, mobile=con, image=i, address=address)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruitersignup.html', d)

def Recruiterlogin(request):
    error=""
    if request.method=='POST':
        e=request.POST['email']
        p=request.POST['pwd']
        user=authenticate(username=e,password=p)
        if user:
            try:
                user1 = RecruiterSignup.objects.get(user=user)
                if user1:
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'recruiterlogin.html',d)
def Recruiterhome(request):
    return render(request ,"recruiterhome.html")
def view_employee(request):
    return render(request, "view_employee.html")
