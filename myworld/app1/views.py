from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.http import HttpResponse , JsonResponse
from django.conf import settings
from .models import * 
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'email.html')

def email(request):
    if request.method == "POST":
        to = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail( subject ,message , settings.EMAIL_HOST_USER,[to], fail_silently=False,)
        return render(request,'send.html')
    else:
        return render (request,'email.html')


