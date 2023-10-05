from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Route
from .forms import RouteForm
# Create your views here.

def add_route(request):
    route=Route.objects.all()
    if request.method=='POST':
        form=RouteForm(request.POST)
        print(request.POST)

        if form.is_valid():
            route_check=form.cleaned_data['route_name']

            for e in route:
                if route_check == e.route_name:
                    return HttpResponse("Route Already Present. Error")
        
            form.save()
            return redirect('list_route')
    else:
        form= RouteForm()  

    return render(request, 'route_add.html', {'form':form}) 


def update_route(request,route_id):
    route=get_object_or_404(Route,route_id=route_id)
    print(route)
    print(type(route))
    val=route.route_name
    print(type(val))
    if request.method=='POST':
        form=RouteForm(request.POST,instance=route)

        if form.is_valid():
            route_check=form.cleaned_data['route_name']
            """
            if route_check==val:
                return HttpResponse("Cant be Updated")
            """
            form.save()
            return redirect('list_route')
    
    else:
        form=RouteForm(instance=route)

    return render(request,'route_update.html',{'form':form,'route':route})

def list_route(request):
    routes = Route.objects.all()
    return render(request,'route_list.html',{'routes': routes})

   
def delete_route(request,route_id):
    #route_obj = Route.objects.filter(route_id=route_id)
    route_obj = get_object_or_404(Route, route_id=route_id)
    print(type(route_obj.route_name))
    
    if request.method == 'POST':
        route_obj.delete()
        return redirect('class_list')
    
    return render(request, 'route_delete.html', {'route_obj': route_obj})
