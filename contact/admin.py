from django.contrib import admin
from contact.models import contactUs


class contactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(contactUs, contactUsAdmin)
