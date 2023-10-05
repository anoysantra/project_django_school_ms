from django.urls import path
from . import views 

urlpatterns = [
    # Add Teacher
    path('add_teacher/<str:dep_id>/', views.add_teacher, name='add_teacher'),

    # List Teachers
    path('list_teacher/', views.list_teacher, name='list_teacher'),

    # Update Teacher
    path('update_teacher/<str:teacher_id>/', views.update_teacher, name='update_teacher'),

    # Delete Teacher
    path('delete_teacher/<str:teacher_id>/', views.delete_teacher, name='delete_teacher'),
]
