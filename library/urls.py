from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.add_book, name='add_book'),
    path('books_list/', views.list_book, name='list_book'),
    path('books_update/<str:book_id>', views.update_book, name='update_book'),
    path('books_delete/<str:book_id>', views.delete_book, name='delete_book'),
]