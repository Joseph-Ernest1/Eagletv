from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Contact
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'news/index.html')

def About(request):
    return render(request, 'news/about.html')

# def Contact(request):
#     return render(request, 'news/contact.html')

def Category(request):
    return render(request, 'news/category.html')


def Contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        name= request.POST.get("name")

        print(email, message, subject, name)

        Contact.objects.create(name=name, email=email, message=message, subject=subject)
        messages.success(request, "Contact created")
        return redirect("/")
    return render(request, "news/contact.html")