from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from .models import SMSLog
from .forms import SMSLogForm

def smslog_list(request):
    sms_logs = SMSLog.objects.all()
    return render(request, 'smslog_list.html', {'sms_logs': sms_logs})

def add_smslog(request):
    if request.method == 'POST':
        form = SMSLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('smslog_list')
    else:
        form = SMSLogForm()
    return render(request, 'smslog_add.html', {'form': form})

def smslog_update(request, sms_id):
    sms_log = get_object_or_404(SMSLog, sms_id=sms_id)

    if request.method == 'POST':
        form = SMSLogForm(request.POST, instance=sms_log)
        if form.is_valid():
            form.save()
            return redirect('smslog_list')
    else:
        form = SMSLogForm(instance=sms_log)

    return render(request, 'smslog_update.html', {'form': form, 'sms_log': sms_log})

def smslog_delete(request, sms_id):
    sms_log = get_object_or_404(SMSLog, sms_id=sms_id)

    if request.method == 'POST':
        sms_log.delete()
        return redirect('smslog_list')

    return render(request, 'smslog_delete.html', {'sms_log': sms_log})
