from django.urls import path
from . import views

urlpatterns = [
    path('dep_add/', views.add_department, name='add_department'),
    path('dep_list/', views.list_department, name='list_department'),
    path('dep_delete/<str:dep_name>',views.delete_department,name='delete_department'),
    path('dep_update/<str:dep_id>',views.update_department,name='update_department'),
]