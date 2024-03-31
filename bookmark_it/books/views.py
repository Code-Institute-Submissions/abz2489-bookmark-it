from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Book


def all_books(request):
    """A view to return the books, sorting & search queries"""

    books = Book.objects.all()
    query = None

    """Search"""
    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            print(f"Query: {query}")
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(author__icontains=query) | Q(summary__icontains=query) | Q(category__name__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
    }
    return render(request, 'books/books.html', context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)
