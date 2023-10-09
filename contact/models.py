from django.db import models


class contactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def _str_(self):
        return self.name