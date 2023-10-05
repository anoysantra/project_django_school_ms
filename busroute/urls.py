from django.urls import path
from . import views

urlpatterns = [
    path('route_add/', views.add_route, name='add_route'),
    path('route_list/', views.list_route, name='list_route'),
    path('route_delete/<str:route_id>',views.delete_route,name='delete_route'),
    path('route_update/<str:route_id>',views.update_route,name='update_route'),
]