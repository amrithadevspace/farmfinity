from django.shortcuts import render,redirect
from krishibhavan.models import Krishibhavan
from login.models import Login
from django.core.files.storage import FileSystemStorage
# Create your views here.

def krishibhavan(request):
    if request.method == 'POST':
        obj=Krishibhavan()
        obj.krishibhavan_name=request.POST.get('krishibhavan name')
        obj.officer_name=request.POST.get('officer name')
        obj.place=request.POST.get('place')
        obj.service_area=request.POST.get('service area')
        obj.district=request.POST.get('district')
        obj.pin=request.POST.get('pin')
        obj.office_address=request.POST.get('office address')
        # obj.office_photo=request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        obj.office_photo = myfile.name
        obj.user_name=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.save()

        k=Login()
        k.username=obj.user_name
        k.password=obj.password
        k.u_id=obj.krishibhavan_id
        k.type='krishibhavan'
        k.save()
        return redirect('/login/login/')
    return render(request,'krishibhavan/krishibhavan register.html')

def  view_krishibhavan(request):
    obj =Krishibhavan.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'krishibhavan/view krishibhavan.html',context)


from django.http import JsonResponse

def krishibhavan_search(request):

    district = request.GET.get('district', '')

    if district == 'all':
        krishibhavans = Krishibhavan.objects.all()
    else:
        krishibhavans = Krishibhavan.objects.filter(district=district)

    data = []

    for i in krishibhavans:
        data.append({
            'krishibhavan_id': i.krishibhavan_id,
            'krishibhavan_name': i.krishibhavan_name,
            'officer_name': i.officer_name,
            'place': i.place,
            'service_area': i.service_area,
            'district': i.district,
            'pin': i.pin,
            'office_address': i.office_address,
            'office_photo': str(i.office_photo),
            'user_name': i.user_name
        })

    return JsonResponse({
        'krishibhavans': data
    })