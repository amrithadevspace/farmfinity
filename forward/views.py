from django.shortcuts import render
from forward.models import  Forward
from farmer.models import Farmer
# Create your views here.

def view_forward(request,idd):
    obj = Farmer.objects.all()
    context = {
        "aa": obj
    }

    if request.method=='POST':
        obj = Forward()
        obj.farmer_id=request.POST.get('yy')
        obj.complaint_id =idd
        obj.save()
    return render(request, 'forward/post  forward.html',context)
