from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def sendemail(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        to = request.POST.get('recipient')
        message = request.POST.get('message')
        # print(to,message)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[to])
        return render(request, 'email.html', {'title': 'send an email'})
    else:
        return render(request, 'email.html',{'title':'send an email'})
