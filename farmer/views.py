from django.shortcuts import render,redirect
from farmer.models import Farmer
from login.models import Login
from django.core.files.storage import FileSystemStorage


# Create your views here.

def farmer(request):

    if request.method=='POST':
        obj=Farmer()
        obj.status='pending'
        obj.farmer_name=request.POST.get('farmername')
        obj.gender=request.POST.get('gender')
        obj.house_name= request.POST.get('housename')
        obj.place = request.POST.get('place')
        obj.post=request.POST.get('post')
        obj.district=request.POST.get('district')
        obj.phone_number=request.POST.get('phonenumber')
        obj.email=request.POST.get('email')
        # obj.photo=request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.photo = myfile.name
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.farming_type=request.POST.get('type')
        obj.save()

        k=Login()
        k.username=obj.username
        k.password=obj.password
        k.u_id=obj.farmer_id
        k.type='farmer'
        k.save()
        return redirect('/login/login/')


    return render(request,'farmer/farmer register.html')

def manage_farmer(request):
    obj=Farmer.objects.all()
    context={
        'aa':obj
    }
    return  render(request,'farmer/manage farmer.html',context)

from django.http import JsonResponse

def farmer_search(request):

    district = request.GET.get('district', '')

    if district == 'all':

        farmers = Farmer.objects.all()

    else:

        farmers = Farmer.objects.filter(
            district=district
        )


    data = []


    for i in farmers:

        data.append({

            'farmer_id': i.farmer_id,

            'farmer_name': i.farmer_name,

            'gender': i.gender,

            'house_name': i.house_name,

            'place': i.place,

            'post': i.post,

            'district': i.district,

            'phone_number': i.phone_number,

            'email': i.email,

            'photo': str(i.photo),

            'username': i.username,

            'farming_type': i.farming_type,

            'status': i.status

        })


    return JsonResponse({

        'farmers': data

    })
def accept(request,idd):
    obj=Farmer.objects.get(farmer_id=idd)
    obj.status='accepted'
    obj.save()
    return manage_farmer(request)

def reject(request,idd):
  obj=Farmer.objects.get(farmer_id=idd)
  obj.status='rejected'
  obj.save()
  return manage_farmer(request)