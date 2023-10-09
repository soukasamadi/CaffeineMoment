from django.db import models


class BannerVertical(models.Model):
    """
    Modal for banner home bottom
    """

    class Meta:
        verbose_name_plural = "Vertical Banner"

    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to="banners/", null=True, blank=True)
    image_small = models.ImageField(
        upload_to="banners/", null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
