from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dormitory
from .forms import DormitoryForm
# Create your views here.

def add_dormitory(request):
    dormitory=Dormitory.objects.all()
    if request.method=='POST':
        form=DormitoryForm(request.POST)
        print(request.POST)

        if form.is_valid():
            dormitory_check=form.cleaned_data['dormitory_name']

            for e in dormitory:
                if dormitory_check == e.dormitory_name:
                    return HttpResponse("Dormitory Already Present. Error")
        
            form.save()
            return redirect('list_dormitory')
    else:
        form= DormitoryForm()  

    return render(request, 'dormitory_add.html', {'form':form}) 

def update_dormitory(request,dormitory_id):
    dormitory=get_object_or_404(Dormitory,dormitory_id=dormitory_id)
    print(dormitory)
    print(type(dormitory))
    val=dormitory.dormitory_name
    print(type(val))
    if request.method=='POST':
        form=DormitoryForm(request.POST,instance=dormitory)

        if form.is_valid():
            dormitory_check=form.cleaned_data['dormitory_name']

            if dormitory_check==val:
                return HttpResponse("Cant be Updated")
            form.save()
            return redirect('list_dormitory')
    
    else:
        form=DormitoryForm(instance=dormitory)

    return render(request,'dormitory_update.html',{'form':form,'dormitory':dormitory})

def list_dormitory(request):
    dormitorys = Dormitory.objects.all()
    return render(request,'dormitory_list.html',{'dormitorys': dormitorys})

   
def delete_dormitory(request,dormitory_id):
    dormitory_obj = Dormitory.objects.filter(dormitory_name=dormitory_id)
    print(dormitory_obj)
    
    if request.method == 'POST':
        dormitory_obj.delete()
        return redirect('list_dormitory')
    
    return render(request, 'dormitory_delete.html', {'dormitory_obj': dormitory_obj})

