from django.db import models
from classes.models import Classes,Section
from students.models import Student
from exam_type.models import Exams
from subjects.models import Subjects


class MarkingStudents(models.Model):
    student_name=models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    section_name = models.ForeignKey(Section, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(Exams, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()

    def __str__(self):
        return str(self.student_name)