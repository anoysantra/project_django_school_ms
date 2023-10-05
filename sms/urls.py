# smslog/urls.py
from django.urls import path
from .views import smslog_list, add_smslog, smslog_update, smslog_delete

urlpatterns = [
    path('smslog/', smslog_list, name='smslog_list'),
    path('smslog/add/', add_smslog, name='add_smslog'),
    path('smslog/<str:sms_id>/update/', smslog_update, name='smslog_update'),
    path('smslog/<str:sms_id>/delete/', smslog_delete, name='smslog_delete'),
]
