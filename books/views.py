from unicodedata import category

from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Book
from .forms import BookForm


def all_books(request):
    """A view to return the books, sorting & search queries"""

    books = Book.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    """Search queries, sorting by title, author, price and category"""
    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "title":
                print(f"Sort Key: {sortkey}")
                sortkey = "lower_title"
                books = books.annotate(lower_title=Lower("title"))

            if sortkey == "author":
                sortkey = "lower_author"
                books = books.annotate(lower_author=Lower("author"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            books = books.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            print(f"Query: {query}")
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse("books"))
            
            queries = Q(title__icontains=query) | Q(author__icontains=query) | Q(summary__icontains=query) | Q(category__name__icontains=query)
            books = books.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "books": books,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting
    }
    return render(request, "books/books.html", context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)


@login_required
def add_book(request):
    """Add a new book to the book shop"""
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can access this page")
        return redirect(reverse("books"))

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, "You successfully added a new book!")
            return redirect(reverse("book_summary", args=[book.id]))
        else:
            messages.error(request, "Unable to upload book. Double check the form and try again.")
    else:
        form = BookForm()
    template = "books/add_book.html"
    context = {
        "form": form,   
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """Edit and existing book"""
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can access this page")
        return redirect(reverse("books"))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f"Changes made to {book.title}")
            return redirect(reverse("book_summary", args=[book.id]))
        else: 
            messages.error(request, "Failed to update the book. Double check the form and try again.")
    else:
        form = BookForm(instance=book)
        messages.info(request, f"Editing {book.title}")

    template = "books/edit_book.html"
    context = {
        "form": form,
        "book": book, 
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """Delete a book from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can delete books")
        return redirect(reverse("books"))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, f"{book.title} successfully deleted")
    return redirect(reverse("books"))