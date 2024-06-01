from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Bookmark
from .forms import UserProfileForm

from books.models import Book
from checkout.models import Order


@login_required
def profile(request):
    """ 
    A view to display a user's profile 
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Delivery info updated successfully")
        else:
            messages.error(request, "Failed to update delivery info. Please check the form is filled out correctly.")
    else:
        form = UserProfileForm(instance=profile)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    A view to display a user's order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def bookmark_add(request, book_id):
    """A view to bookmark selected books"""
    book = get_object_or_404(Book, id=book_id)
    Bookmark.objects.get_or_create(user=request.user, book=book)
    messages.success(request, f"Successfully bookmarked {book.title}")

    return redirect("book_summary", book_id=book_id)


@login_required
def bookmark(request):
    """A view to display user's bookmarked books"""
    bookmarks = Bookmark.objects.filter(user=request.user)
    user_bookmarks = [bookmark.book for bookmark in bookmarks]

    template = "profiles/bookmarks.html"
    context = {
        "user_bookmarks": user_bookmarks
    }
    return render(request, template, context)