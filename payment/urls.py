from django.urls import path
from . import views

urlpatterns = [
    path('payment_add/', views.add_payment, name='add_payment'),
    path('payment_list/', views.list_payment, name='list_payment'),
    path('payment_delete/<str:payment_id>',views.delete_payment,name='delete_payment'),
    path('payment_update/<str:payment_id>',views.update_payment,name='update_payment'),
]