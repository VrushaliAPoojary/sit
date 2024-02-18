from django.shortcuts import render
from core.models import Event  
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import re

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('name') 
        from_email = request.POST.get('email') 
        img = request.FILES.get('photo')  # Change to request.FILES to get uploaded files
        print("From Email:", from_email)
        
        if re.match(r'^[\w\.-]+@[\w\.-]+$', from_email):
            email_username = from_email.split('@')[0]
            print(email_username)

            # Create an EmailMessage object
            email = EmailMessage(
                subject=f'{fname}',
                body=f'Here is the message. {fname} {from_email}',
                from_email=settings.EMAIL_HOST_USER,
                to=['snapship43@gmail.com'],  # Replace with your recipient's email address
                cc=[],  # Add CC email addresses if needed
            )
            # Attach the image file to the email
            email.attach(img.name, img.read(), img.content_type)
            email.send()  # Send the email

            fevent = Event(name=fname, email=from_email)  
            fevent.save() 
            messages.success(request, "Profile details updated.")
        else:
            messages.error(request, "Invalid email address")
    return render(request, 'book.html')


def about(request):
    return render(request,'about.html' )

def contact(request):
    return render(request,'contact.html' )
