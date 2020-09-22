from django.shortcuts import render,redirect
from .models import Doctor,Customer,Appointment,Contact,Treatment
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    doctors=Doctor.objects.all()
    customers=Customer.objects.all()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        doctors=request.POST['doctors']
        date=request.POST['date']
        time=request.POST['time']
        email=request.POST['email']
        doctor_email=request.POST['doctor_email']
        send_mail(
            'Appointment',
            'Some Paitent have been qruies in website.',
            'my444323@gmail.com',
            [doctor_email,'yf20122001@gmail.com'],
        )
        appointment=Appointment(first_name=first_name,last_name=last_name,doctors=doctors,time=time,date=date,email=email,doctor_email=doctor_email)
        appointment.save()
        messages.success(request,'Your appointment request has been submitted and admin will contact you if this approve or not')

        return redirect('home')


    context={
        'doctors':doctors,
        'customers':customers,
    }
    return render(request,'app/index.html',context)
def about(request):
    return render(request,'app/about.html')
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,'Thank you so much! Your form has been submitted soon admin will contact you')
        return redirect('contact')

    return render(request,'app/contact.html')
def doctor(request):
    doctors=Doctor.objects.all()
    context={
        'doctors':doctors,
    }
    return render(request,'app/doctor.html',context)
def department(request):
    treatments=Treatment.objects.all()
    context={
        'treatments':treatments
    }
    return render(request,'app/department.html',context)
def pricing(request):
    return render(request,'app/pricing.html')
