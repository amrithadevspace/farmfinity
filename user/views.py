from django.shortcuts import render,redirect
from user.models import User
from login.models import Login
# Create your views here.

def user(request):
    if request.method=='POST':
        obj=User()
        obj.name= request.POST.get('name')
        obj.gender= request.POST.get('gender')
        obj.place = request.POST.get('place')
        obj.post= request.POST.get('post')
        obj.district= request.POST.get('district')
        obj.pin = request.POST.get('pin')
        obj.phone_number = request.POST.get('phone_number')
        obj.email = request.POST.get('email')
        obj.username = request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.save()

        k=Login()
        k.username=obj.username
        k.password=obj.password
        k.u_id=obj.user_id
        k.type='user'
        k.save()
        return redirect('/login/login/')
    return render(request,'user/user register.html')

def view_user(request):
    obj = User.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'user/view user.html',context)
