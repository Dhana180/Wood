from django.shortcuts import render
from .models import quotations
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def project(request):
    return render(request,'project.html')

def quote(request):
    return render(request,'quote.html')

def contact(request):
    return render(request,'contact.html')

def booking(request):

    mails=[i.mail for i in quotations.objects.all()]

    if request.method=='POST':
        username=request.POST['uname']
        usermail=request.POST['umail']
        usercontact=request.POST['mobile']
        userservice=request.POST['service']
        userbudget=request.POST['budget']
        usernote=request.POST['note']


        if usermail in mails:
            messages.info(request,"Mail Already Exists")


        record = quotations.objects.create(name=username,mail=usermail,contact=usercontact,service=userservice,budget=userbudget,note=usernote)

        record.save()
        
    
    else:
        return render(request,'quote.html')
    
    return render(request,'quote.html')
