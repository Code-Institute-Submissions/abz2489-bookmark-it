from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book



def basket_contents(request):

    """Context processor for basket contents to make them available across the whole site"""

    basket_items = []
    total_price = 0
    number_of_books = 0
    basket = request.session.get("basket", {})

    for book_id, quantity in basket.items():
        book = get_object_or_404(Book, id=book_id)
        total_price += quantity * book.price
        number_of_books += quantity
        basket_items.append({
            "book_id": book_id,
            "quantity": quantity,
            "book": book,
            "total_price": total_price
        })

    if total_price < settings.FREE_DELIVERY:
        delivery = total_price * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total_price
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total_price

    context = {
        "basket_items": basket_items,
        "total_price": total_price,
        "number_of_books": number_of_books,
        "delivery": delivery,
        "free_delivery": settings.FREE_DELIVERY,
        "free_delivery_delta": free_delivery_delta,
        "grand_total": grand_total
    }
    return context