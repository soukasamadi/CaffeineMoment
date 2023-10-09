from django.contrib import admin

from .models import BannerVertical


@admin.register(BannerVertical)
class BannerVertical(admin.ModelAdmin):
    """
    Displays the Banner Vertical model in the admin panel
    """

    list_display = (
        "name",
        "description",
        "image_small",
        "featured",
    )
