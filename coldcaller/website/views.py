

from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl_context
ssl._create_default_https_context = ssl._create_unverified_context

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name,email=email,message=message)
        # send_mail(
        #     subject=f"New Contact Form Submission from {name}",
        #     message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
        #     from_email="omshivadigital@gmail.com",  
        #     recipient_list=["ashokcivil27@gmail.com"],  
        #     fail_silently=False,
        # )

        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect("contact")  # reload page so form is cleared

    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
