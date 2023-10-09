from .models import *


def banner_vertival(request):
    """
    A view to dispaly a vertical banner
    """
    banner_vertival = BannerVertical.objects.filter(featured=True)

    context = {
        "banner_vertival": banner_vertival,
    }

    return context
