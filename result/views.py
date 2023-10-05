from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse
from classes.models import Classes, Section


from students.models import Student
from . models import MarkingStudents
from .forms import MarkingStudentsForm,StudentSearchMarksForm


def SearchMarksStudent(request):

    if request.method=='POST':
        form=StudentSearchMarksForm(request.POST)

        if form.is_valid():
            class_name=form.cleaned_data['class_name'].class_name
            section_name=form.cleaned_data['section_name'].section_name
            student_name=form.cleaned_data['student_name'].name

            print(class_name,section_name,student_name,type(class_name),type(section_name),type(student_name))
            try:
                class_n=get_object_or_404(Classes,class_name=class_name)      
                section=get_object_or_404(Section,class_name=class_name,section_name=section_name)
                print("*")
                student_name=get_object_or_404(Student,class_name=class_name,section_name=section_name,name=student_name)
                print('#')
            except:
                return HttpResponse("No student found With that Details")
        
            
            class_val=class_n.class_name
            section_val=section.section_name
            student_name_val=student_name.name
            
            print(class_val,section_val,student_name_val,type(class_val),type(section_val),type(student_name_val))
            if class_name!=class_val and section_name!=section_val :
                return HttpResponse("Such Student not found")
        
            return redirect(reverse('stu_marks_entry',args=[class_name,section_name,student_name]))
        
    else:
        form= StudentSearchMarksForm()

    return render(request,'search_for_marks.html',{'form':form})


def stu_marks_entry(request,class_name,section_name,student_name):
    
    if request.method == 'POST':
        form = MarkingStudentsForm(request.POST)
        if form.is_valid():
            class_name_check=form.cleaned_data['class_name'].class_name
            section_name_check=form.cleaned_data['section_name'].section_name
            student_name_check=form.cleaned_data['student_name'].name
            print(class_name_check, section_name_check, section_name_check)
            
            if section_name_check!=section_name or class_name_check!=class_name or student_name_check!=student_name:
                return HttpResponse("<h1>No such student entry allowed Enter corrrect Data")

            form.save()
            return redirect('marking_students_detail')  # Redirect to a success page
    else:
        form = MarkingStudentsForm(initial={'class_name':class_name,'section_name':section_name,'student_name':student_name})

    return render(request, 'marks_entry.html', {'form': form,'class_name': class_name, 'section_name': section_name, 'student_name': student_name})


def marking_students_list(request):
    marking_students = MarkingStudents.objects.all()
    print(marking_students)
    return render(request, 'marking_students_list.html', {'marking_students': marking_students})



def stu_marks_update(request, student_name):
    marking_student = get_object_or_404(Student, name=student_name)
    stu= get_object_or_404(MarkingStudents, student_name=marking_student)
    val1=marking_student.name
    val2=marking_student.class_name
    val3=marking_student.section_name
    print(marking_student.name,marking_student.class_name,marking_student.section_name,type(marking_student.name),type(marking_student.class_name),type(marking_student.section_name))


    if request.method == 'POST':
        form = MarkingStudentsForm(request.POST,instance=stu)
        if form.is_valid():
            class_check=form.cleaned_data['class_name'].class_name
            section_check=form.cleaned_data['section_name'].section_name
            name_check=form.cleaned_data['student_name'].name
            print(class_check,section_check,name_check,type(class_check),type(name_check))
            print(val1,val2,val3,type(val2),type(val1),type(val3))

            if class_check!=val2 or name_check!=val1 or section_check!=val3:
                return HttpResponse("Try Updating with Same Value of the Candidate/Student")
            
            form.save()
            
            return redirect('marking_students_detail')
    else:
        form = MarkingStudentsForm(instance=stu)

    return render(request, 'marks_update.html', {'form': form, 'marking_student': stu})


def stu_marks_delete(request, student_name):
    marking_student = get_object_or_404(Student, name=student_name)
    if request.method == 'POST':
        marking_student.delete()
        return redirect('marking_students_detail')

    return render(request, 'marks_delete.html', {'marking_student': marking_student})






