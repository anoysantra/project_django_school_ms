from django.urls import path
from . import views 

urlpatterns = [
    path('entry/<str:class_name>/<str:section_name>/<str:student_name>', views.stu_marks_entry, name='stu_marks_entry'),
    # Add other URLs as needed

    path('entry/',views.SearchMarksStudent,name='search_student_for_marks'),
    path('markingstudents/', views.marking_students_list, name='marking_students_detail'),
    path('update_markingstudents/<str:student_name>', views.stu_marks_update, name='stu_marks_update'),
    path('delete_markingstudents/<str:student_name>', views.stu_marks_delete, name='delete_marks'),
]