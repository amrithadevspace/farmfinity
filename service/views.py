from django.shortcuts import render
from service.models import Service
import datetime
# Create your views here.

def service(request):
   ss=request.session['u_id']
   if request.method=='POST':
        obj=Service()
        obj.krishibhavan_id=ss
        obj.date=datetime.datetime.today()
        obj.service_name = request.POST.get('service')
        obj.discription = request.POST.get('description')
        obj.phone_number = request.POST.get('contact')
        obj.save()
   return render(request,'service/post service.html')

def view_service(request):
    obj =Service.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'service/view service.html',context)

def view_service2(request):
    obj =Service.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'service/view service2.html',context)