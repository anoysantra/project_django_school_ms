from django.urls import path
from . import views

urlpatterns = [
    path('dormitory_add/', views.add_dormitory, name='add_dormitory'),
    path('dormitory_list/', views.list_dormitory, name='list_dormitory'),
    path('dormitory_delete/<str:dormitory_id>',views.delete_dormitory,name='delete_dormitory'),
    path('dormitory_update/<str:dormitory_id>',views.update_dormitory,name='update_dormitory'),
]