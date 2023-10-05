from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
from .forms import StudentForm,StudentSearchForm
from classes.models import Classes,Section

def SearchStudent(request):

    if request.method=='POST':
        form=StudentSearchForm(request.POST)

        if form.is_valid():
            class_name=form.cleaned_data['class_name']
            section_name=form.cleaned_data['section_name']
            class_n=get_object_or_404(Classes,class_name=class_name)
            #print(type(class_n))
            section=get_object_or_404(Section,class_name=class_name,section_name=section_name)
            #print(type(section))
            class_val=class_n.class_name
            section_val=section.section_name
            #if class_n and section:
            if class_name!=class_val and section_name!=section_val:
                return HttpResponse("Such Class and Section not found")
        
            return redirect(reverse('add_student',args=[class_name,section_name]))
        
    else:
        form= StudentSearchForm()

    return render(request,'search_student.html',{'form':form})
            
            


def add_student(request,class_name,section_name):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm(initial={'class_name':class_name,'section_name':section_name})
    return render(request, 'add_student.html', {'form': form})


def list_student(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})


def update_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    val_check=student.student_id

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            student_id_check=form.cleaned_data['student_id']
            class_name=form.cleaned_data['class_name']
            section_name=form.cleaned_data['section_name']

            class_n=get_object_or_404(Classes,class_name=class_name)
            #print(type(class_n))
            section=get_object_or_404(Section,class_name=class_name,section_name=section_name)
            #print(type(section))
            class_val=class_n.class_name
            section_val=section.section_name
            #if class_n and section:
            if class_name!=class_val and section_name!=section_val:
                return HttpResponse("Such Class and Section not found To Update")
            

            if val_check != student_id_check:
                print("Check Condition")
                return HttpResponse("<h1>Update of Id not allowed. Create a new one with Specified Id")
            
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_student')
    return render(request, 'delete_student.html', {'student': student})
