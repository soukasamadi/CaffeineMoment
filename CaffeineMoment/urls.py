from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404


urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls"), name="accounts.urls"),
    path("products/", include("products.urls"), name="products.urls"),
    path("bag/", include("bag.urls"), name="bag.urls"),
    path("profile/", include("profiles.urls"), name="profile.urls"),
    path("checkout/", include("checkout.urls"), name="checkout.urls"),
    path("reviews/", include("reviews.urls"), name="reviews.urls"),
    path("contact/", include("contact.urls"), name="contact.urls"),
    path("", include("banners.urls"), name="banners.urls"),
    path("summernote/", include("django_summernote.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

HANDLER404 = "CaffeineMoment.views.handler404"
