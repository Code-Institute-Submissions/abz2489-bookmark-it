from django.shortcuts import render

# Create your views here.

def all_books(request):
    """A view to return the books page"""
    return render(request, 'books/books.html')
