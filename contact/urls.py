from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('ajax_contact_form/', views.ajax_contact_form, name='ajax_contact_form'),
]
