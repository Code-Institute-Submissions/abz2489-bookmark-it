from django.shortcuts import render
from . import views

def view_basket(request):
    """A view that renders basket items page"""

    return render(request, "basket/basket.html")
