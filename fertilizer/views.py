from django.shortcuts import render
from fertilizer.models import Fertilizer
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.

def fertilizer (request):
    ss=request.session['u_id']
    if request.method == 'POST':
        obj=Fertilizer()
        obj.krishibhavan_id=ss
        obj.date=datetime.datetime.today()
        obj.fertilizer_name=request.POST.get('fertilizer name')
        obj.discription=request.POST.get('description')
        obj.type=request.POST.get('type')
        obj.price=request.POST.get('price')
        obj.unit=request.POST.get('unit')
        obj.manufacturing_company=request.POST.get('manufacturing')
        # obj.image=request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.photo = myfile.name
        obj.phone_number=request.POST.get('phone')
        obj.save()
    return render(request,'fertilizer/post fertilizer.html')


def view_fertilizer (request):
    obj =Fertilizer.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'fertilizer/view fertilizer.html',context)