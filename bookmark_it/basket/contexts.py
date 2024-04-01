from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    """Context processor for basket contents to make them available across the whole site"""

    basket_items = []
    total_price = 0
    number_of_books = 0

    if total_price < settings.FREE_DELIVERY:
        free_delivery = total_price * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total_price
    else:
        free_delivery = 0
        free_delivery_delta = 0

    grand_total = free_delivery + total_price

    context = {
        "basket_items": basket_items,
        "total_price": total_price,
        "number_of_books": number_of_books,
        "free_delivery": settings.FREE_DELIVERY,
        "free_delivery_delta": free_delivery_delta,
        "grand_total": grand_total
    }
    return context