from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    summary = models.TextField(max_length=1000)
    author = models.CharField(max_length=254)
    isbn = models.BigIntegerField(unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(null=True, blank=True)
    series = models.CharField(max_length=254, null=True, blank=True)
    number_in_series = models.IntegerField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
