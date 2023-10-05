from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from department.models import Department

def add_teacher(request,dep_id):
    dep=get_object_or_404(Department, dep_id=dep_id)
    val=dep.dep_name
    print(val,type(val))

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
        
            dep_id_check = form.cleaned_data['dep_id']
            
            dep_name_check=get_object_or_404(Department,dep_id=dep_id_check)
            name=dep_name_check.dep_name
            if val!=name:
                return HttpResponse('<h1>Cant be added.No such Departments</h1>')
            
            form.save()
            return redirect('list_teacher')
    else:
        form=TeacherForm()
        #form = TeacherForm(initial={'class_name':class_name,'section_name':section_name})
    return render(request, 'add_teacher.html', {'form': form})


def list_teacher(request):
    teachers = Teacher.objects.all()
    print(teachers,type(teachers))
    return render(request, 'list_teacher.html', {'teachers': teachers})


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    val_check=teacher.teacher_id

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            teacher_id_check=form.cleaned_data['dep_name']
            """
            if val_check != teacher_id_check:
                print("Check Condition")
                return HttpResponse("<h1>Update of Id not allowed. Create a new one with Specified Id")
            """
            form.save()
            return redirect('list_teacher')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'update_teacher.html', {'form': form, 'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('list_teacher')
    return render(request, 'delete_teacher.html', {'teacher': teacher})


