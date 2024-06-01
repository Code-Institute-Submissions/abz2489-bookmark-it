from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('bookmark_add/int:<book_id>/', views.bookmark_add ,name='bookmark_add'),
    path('bookmark/', views.bookmark, name='bookmark'),
]