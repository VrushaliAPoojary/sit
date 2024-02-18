from django.shortcuts import render
from core.models import Event  
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import re

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('name') 
        from_email = request.POST.get('email') 
        print("From Email:", from_email)
        
        
        if re.match(r'^[\w\.-]+@[\w\.-]+$', from_email):
            
            email_username = from_email.split('@')[0]
            print(email_username)
            send_mail(
                f'{fname}',
                "Here is thesafsd message.",
                f'{email_username}@gmail.com',  
                ['snapship43@gmail.com'],  
                fail_silently=False,
            )
            fevent = Event(name=fname, email=from_email)  
            fevent.save() 
            messages.success(request, "Profile details updated.")
        else:
           
            messages.error(request, "Invalid email address")
    return render(request, 'index.html')
