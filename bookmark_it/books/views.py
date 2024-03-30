from django.shortcuts import render,get_object_or_404
from .models import Book


def all_books(request):
    """A view to return the books, sorting & search queries"""

    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)
