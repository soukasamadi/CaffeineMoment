from .models import *


def products_selected(request):
    """A view to show products selected"""
    products_selected = Product.objects.filter(featured=True)

    context = {
        "products_selected": products_selected,
    }

    return context


def products_sales(request):
    """A view to show sales products"""
    products_sales = Product.objects.filter(product_status__name="Sales")

    context = {
        "products_sales": products_sales,
    }

    return context
