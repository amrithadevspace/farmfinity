from django.shortcuts import render
from complaint.models import Complaint
from farmer.models import Farmer
from forward.models import Forward
import datetime


# Create your views here.
# 
def complaint (request):
    ss=request.session['u_id']
    if request.method=="POST":
        obj=Complaint()
        obj.user_id =ss
        obj.complaint=request.POST.get("complaint")
        obj.date=datetime.datetime.today()
        obj.reply="pending"
        obj.type='user'
        obj.save()
    return render(request,'complaint/post complaint.html')

def view_complaint(request):

    obj = Complaint.objects.filter(type='user')
    context={
        "aa":obj
    }
    return render(request,'complaint/view complaint.html',context)

def post_reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()

    return render(request, 'complaint/post reply.html')


def view_reply(request):
    obj = Complaint.objects.filter(type='admin')
    context = {
        "aa": obj
    }
    return render(request, 'complaint/view reply.html', context)


def complaint2 (request):
    ss=request.session['u_id']
    if request.method=="POST":
        obj=Complaint()
        obj.farmer_id=ss
        obj.complaint=request.POST.get("complaint2")
        obj.date=datetime.datetime.today()
        obj.reply="pending"
        obj.type='farmer'
        obj.save()
    return render(request,'complaint/post complaint 2.html')

def view_complaint2(request):

    obj = Complaint.objects.filter(type='farmer')
    context={
        "aa":obj
    }
    return render(request,'complaint/view complaint 2.html',context)

def post_reply2(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()

    return render(request, 'complaint/post reply 2.html')


def view_reply2(request):
    obj = Complaint.objects.filter(type='farmer')
    context = {
        "aa": obj
    }
    return render(request, 'complaint/view reply 2.html', context)


def farmer_complaint(request):
    obj = Farmer.objects.all()
    context = {
        "aa": obj
    }
    ss=request.session['u_id']
    if request.method=='POST':
        obj = Complaint()
        obj.user_id= ss
        obj.farmer_id=request.POST.get('yy')
        obj.complaint = request.POST.get("complaint")
        obj.date = datetime.datetime.today()
        obj.reply = 'pending'
        obj.type='user farmer'
        obj.save()
    return render(request, 'complaint/post farmer complaint.html',context)

def view_farmer_complaint(request):
    obj = Complaint.objects.filter(type='user farmer')
    context = {
        "aa": obj
    }
    return render(request, 'complaint/view farmer complaint.html', context)

def view_farmer_complaint2(request):
    ss=request.session['u_id']
    obj = Forward.objects.filter(farmer_id=ss)
    context = {
        "aa": obj
    }
    return render(request, 'complaint/view farmer complaint2.html', context)


def farmer_reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()

    return render(request, 'complaint/post farmer reply.html')


def view_farmer_reply(request):
    ss = request.session['u_id']
    obj = Complaint.objects.filter(user_id=ss)
    context = {
        "aa": obj
    }
    return render(request, 'complaint/view farmer reply.html', context)
