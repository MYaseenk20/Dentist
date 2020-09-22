from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    fields=models.CharField(max_length=200,null=True,blank=True)
    slogan=models.CharField(max_length=200,null=True,blank=True)
    picture=models.ImageField(null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    reviews=models.TextField()
    customer=models.CharField(max_length=200,null=True,blank=True)
    occupation=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.customer
class Contact(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    message=models.TextField()
class Appointment(models.Model):
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=200,null=True,blank=True)
    date=models.CharField(max_length=200,null=True,blank=True)
    time=models.CharField(max_length=200,null=True,blank=True)
    doctors=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    doctor_email=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.doctors
class Treatment(models.Model):
    picture=models.ImageField(null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    explanation=models.TextField()
    def __str__(self):
        return self.name
