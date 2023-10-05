from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.add_emp, name='add_emp'),
    path('emp_list/', views.list_emp, name='list_emp'),
    path('emp_update/<str:category_id>', views.update_emp, name='update_emp'),
    path('emp_delete/<str:category_id>', views.delete_emp, name='delete_emp'),
]