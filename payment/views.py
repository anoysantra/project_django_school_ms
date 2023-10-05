from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Payment
from .forms import PaymentForm
# Create your views here.

def add_payment(request):
    payment=Payment.objects.all()
    if request.method=='POST':
        form=PaymentForm(request.POST)
        print(request.POST)

        if form.is_valid():
            payment_check=form.cleaned_data['payment_name']

            for e in payment:
                if payment_check == e.payment_name:
                    return HttpResponse("Payment Already Present. Error")
        
            form.save()
            return redirect('list_payment')
    else:
        form= PaymentForm()  

    return render(request, 'payment_add.html', {'form':form}) 

def update_payment(request,payment_id):
    payment=get_object_or_404(Payment,payment_id=payment_id)
    print(payment)
    print(type(payment))
    val=payment.payment_name
    print(type(val))
    if request.method=='POST':
        form=PaymentForm(request.POST,instance=payment)

        if form.is_valid():
            payment_check=form.cleaned_data['payment_name']

            if payment_check==val:
                return HttpResponse("Cant be Updated")
            form.save()
            return redirect('list_payment')
    
    else:
        form=PaymentForm(instance=payment)

    return render(request,'payment_update.html',{'form':form,'payment':payment})

def list_payment(request):
    payments = Payment.objects.all()
    return render(request,'payment_list.html',{'payments': payments})

   
def delete_payment(request,payment_id):
    #payment_obj = Payment.objects.filter(payment_id=payment_id)
    payment_obj=get_object_or_404(Payment,payment_id=payment_id)
    print(payment_obj)
    print("here")
    
    if request.method == 'POST':
        payment_obj.delete()
        return redirect('list_payment')
    
    return render(request, 'payment_delete.html', {'payment_obj': payment_obj})
