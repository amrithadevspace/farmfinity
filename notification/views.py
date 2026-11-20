from django.shortcuts import render
from notification.models import Notification
import datetime

# Create your views here.

def notification (request):
    ss=request.session['u_id']
    if request.method == 'POST':
        obj=Notification()
        obj.krishibhavan_id=ss
        obj.notification=request.POST.get('notification')
        obj.date=datetime.datetime.today()
        obj.save()
    return render(request,'notification/post notification.html')

def view_notification(request):
    obj=Notification.objects.all()
    context={
        'aa':obj
    }
    return render(request,'notification/view notification.html',context)

def view_notification2(request):
    obj=Notification.objects.all()
    context={
        'aa':obj
    }
    return render(request,'notification/view notification2.html',context)