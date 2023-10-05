from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.SearchStudent,name='search_student'),
    path('student/<str:class_name>/<str:section_name>', views.add_student, name='add_student'),
    path('student_list/', views.list_student, name='list_student'),
    path('student_update/<str:student_id>', views.update_student, name='update_student'),
    path('student_delete/<str:student_id>', views.delete_student, name='delete_student'),
]