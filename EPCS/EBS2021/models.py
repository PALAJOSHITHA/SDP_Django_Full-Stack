from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class UserSignup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField(null=True)
    address = models.CharField(max_length=300,null=True,default=None)
    regdate = models.DateTimeField(auto_now_add=True,blank=True)
    def _str_(self):
      return self.user.username
class add_Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField(null=True)
    address = models.CharField(max_length=300,null=True,default=None)
    regdate = models.DateTimeField(auto_now_add=True,blank=True)
    def _str_(self):
      return self.user.username

class Job(models.Model):
    jobname=models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    IndustryPractices=models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    venue=models.CharField(max_length=300,null=True)
    entryprice=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.jobname

class SponsorTbl(models.Model):
    job =models.ForeignKey(Job,on_delete=models.CASCADE)
    sponsorimage = models.FileField(null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.job.jobname

class Category(models.Model):
    categoryname=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
      return self.categoryname

class Booking(models.Model):
    userinfo =models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    eventinfo = models.ForeignKey(Job, on_delete=models.CASCADE)
    person=models.CharField(max_length=100,null=True)
    total=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=20,null=True)
    bookingdate = models.DateField(null=True)
    cardno = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=10,null=True)
    expirydate = models.CharField(max_length=50,null=True)
    def _str_(self):
      return self.id

class RecruiterRegistration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    #gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    #gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    #dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def str(self):
        return self.username

    class Meta:
        db_table = "recruiterregistration_table"