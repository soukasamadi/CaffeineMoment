from django.db import models


class Category(models.Model):
    """
    Modal for categories
    """
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductStatus(models.Model):
    """
    Modal for product status
    """
    class Meta:
        verbose_name_plural = 'Product Status'
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Modal for product
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    product_details = models.TextField()
    features = models.TextField()
    old_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='products_images/', null=True, blank=True)
    product_status = models.ForeignKey(
        "ProductStatus", null=True, blank=True, on_delete=models.SET_NULL)
    featured = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)

    def __str__(self):
        return self.name
