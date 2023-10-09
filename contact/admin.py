from django.contrib import admin
from contact.models import Contact


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


admin.site.register(Contact, ContactUsAdmin)
