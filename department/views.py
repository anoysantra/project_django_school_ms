from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Department
from .forms import DepartmentForm
# Create your views here.

def add_department(request):
    department=Department.objects.all()
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        print(request.POST)

        if form.is_valid():
            dep_check=form.cleaned_data['dep_name']

            for e in department:
                if dep_check == e.dep_name:
                    return HttpResponse("Department Already Present. Error")
        
            form.save()
            return redirect('list_department')
    else:
        form= DepartmentForm()  

    return render(request, 'department_add.html', {'form':form}) 

def update_department(request,dep_id):
    dep=get_object_or_404(Department,dep_id=dep_id)
    print(dep)
    print(type(dep))
    val=dep.dep_name
    print(type(val))
    if request.method=='POST':
        form=DepartmentForm(request.POST,instance=dep)

        if form.is_valid():
            dep_check=form.cleaned_data['dep_name']

            if dep_check==val:
                return HttpResponse("Cant be Updated")
            form.save()
            return redirect('class_list')
    
    else:
        form=DepartmentForm(instance=dep)

    return render(request,'department_update.html',{'form':form,'dep':dep})

def list_department(request):
    departments = Department.objects.all()
    return render(request,'department_list.html',{'departments': departments})

   
def delete_department(request,dep_name):
    dep_obj = Department.objects.filter(dep_name=dep_name)
    print(dep_obj)
    
    if request.method == 'POST':
        dep_obj.delete()
        return redirect('class_list')
    
    return render(request, 'department_delete.html', {'dep_obj': dep_obj})
