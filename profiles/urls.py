from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('bookmark_add/int:<book_id>/', views.bookmark_add, name='bookmark_add'),
    path('user_bookmark/', views.user_bookmark, name='user_bookmark'),
    path('bookmark_remove/int:<book_id>/', views.bookmark_remove, name='bookmark_remove'),
]