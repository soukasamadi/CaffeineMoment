from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from contact.models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_contact = Contact(name=name, email=email, message=message)
        new_contact.save()
        messages.success(request, 'Thank you for contacting us. We will get back to you.')        
    return render(request, "contact/contact.html")
