from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_emp')
    else:
        form = EmployeeForm()
    return render(request, 'add_emp.html', {'form': form})


def list_emp(request):
    emps = Employee.objects.all()
    return render(request, 'list_emp.html', {'emps': emps})


def update_emp(request, category_id):
    emp = get_object_or_404(Employee, category_id=category_id)
    val_check=emp.category_id

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)

        if form.is_valid():
            category_id_check=form.cleaned_data['category_id']

            if val_check != category_id_check:
                print("Check Condition")
                return HttpResponse("<h1>Update of Id not allowed. Create a new one with Specified Id")
            
            form.save()
            return redirect('list_emp')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'update_emp.html', {'form': form, 'emp': emp})


def delete_emp(request, category_id):
    emp = get_object_or_404(Employee, category_id=category_id)
    if request.method == 'POST':
        emp.delete()
        return redirect('list_emp')
    return render(request, 'delete_emp.html', {'emp': emp})


