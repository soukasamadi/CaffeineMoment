from django.shortcuts import render


def video_banner(request):
    """
    view to return the home page
    """
    return render(request, "banners/banner_video.html")