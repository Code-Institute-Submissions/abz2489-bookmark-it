from django.contrib import admin
from .models import Category, Book

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name"
    )
    
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "isbn",
        "title",
        "author",
        "price",
        "category",
        "cover"
    )

    ordering = ("id",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)