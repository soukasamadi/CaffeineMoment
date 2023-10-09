from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_contact = Contact(name=name, email=email, message=message)
        new_contact.save()
        success = 'Thank you for contacting us. We will get back to you.'
        return HttpResponse(success)
    return render(request, "contact/contact.html")
