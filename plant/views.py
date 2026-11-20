from django.shortcuts import render
from plant.models import Plant
import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.

def plant (request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Plant()
        obj.krishibhavan_id=ss
        obj.date=datetime.datetime.today()
        obj.plant_name=request.POST.get('plant name')
        obj.category=request.POST.get('category')
        obj.discription=request.POST.get('description')
        obj.growing_season=request.POST.get('season')
        # obj.photo=request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.photo = myfile.name
        obj.phone_number=request.POST.get('phone')
        obj.price=request.POST.get('price')
        obj.save()

    return render(request,'plant/post plant.html')

def view_plant(request):
    obj =Plant.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'plant/view plant.html',context)
def view_plant2(request):
    obj =Plant.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'plant/view plant2.html',context)

