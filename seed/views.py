from django.shortcuts import render
from seed.models import Seed
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.

def seed(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Seed()
        obj.krishibhavan_id=ss
        obj.date=datetime.datetime.today()
        obj.seed_name=request.POST.get('seed name')
        obj.type =request.POST.get('type')
        obj.crop_name = request.POST.get('crop name')
        obj.discription = request.POST.get('description')
        obj.price= request.POST.get('price')
        obj.unit= request.POST.get('unit')
        obj.pnone_number= request.POST.get('phone')
        # obj.photo= request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.photo = myfile.name
        obj.save()

    return render(request,'seed/post seed.html')

def  view_seed(request):
    obj =Seed.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'seed/view seed.html',context)
def  view_seed2(request):
    obj =Seed.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'seed/view seed2.html',context)
