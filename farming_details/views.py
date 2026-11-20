from django.shortcuts import render
from farming_details.models import FarmingDetails
from django.core.files.storage import FileSystemStorage

# Create your views here.

def post_farming (request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=FarmingDetails()
        obj.farmer_id= ss
        obj.article=request.POST.get('article')
        # obj.video=request.POST.get('video')
        fs = FileSystemStorage()

        # Video upload
        video = request.FILES.get('video')
        if video:
            video_name = fs.save(video.name, video)
            obj.video = video_name

        # Article upload
        article = request.FILES.get('article')
        if article:
            article_name = fs.save(article.name, article)
            obj.article = article_name
        obj.crop_name=request.POST.get('crop name')
        obj.status='pending'
        obj.discription=request.POST.get('description')
        obj.type='farmer'
        obj.save()

    return render(request, 'farming_details/post farming farmer.html')

def post_farming_krishibhvan(request):
    ss = request.session['u_id']

    if request.method == 'POST':

        obj = FarmingDetails()
        obj.krishibhavan_id = ss
        obj.crop_name = request.POST.get('crop name')
        obj.discription = request.POST.get('description')
        obj.status = "pending"
        obj.type = "krishibhavan"
        # obj.office_photo=request.POST.get('photo')
        # obj.video=request.POST.get('video')
        fs = FileSystemStorage()

        # Video upload
        video = request.FILES.get('video')
        if video:
            video_name = fs.save(video.name, video)
            obj.video = video

        # Article upload
        article = request.FILES.get('article')
        if article:
            article = fs.save(article.name, article)
            obj.article = article

        obj.save()

    return render(request, 'farming_details/post farming krishi.html')


def view_farming(request):
    obj =FarmingDetails.objects.filter(type='farmer',status='accepted')
    context = {
        "aa": obj
    }
    return render(request, 'farming_details/view farming farmer.html', context)

def view_farming_krishi(request):
    obj=FarmingDetails.objects.filter(type='krishibhavan',status='accepted')
    context ={
        "aa" :obj
    }
    return render(request,'farming_details/view farming krishi.html',context)

def manage_farming(request):
    obj =FarmingDetails.objects.all()
    context = {
        "aa": obj
    }
    return render(request, 'farming_details/manage farming by farmer.html', context)

def manage_farming_krishi(request):
    obj =FarmingDetails.objects.all()
    context = {
        "aa": obj
    }
    return render(request, 'farming_details/manage farming by krishi.html', context)

def accept(request,idd):
    obj=FarmingDetails.objects.get(farming_details_id=idd)
    obj.status='accepted'
    obj.save()
    return manage_farming(request)

def reject(request,idd):
     obj=FarmingDetails.objects.get(farming_details_id=idd)
     obj.status='rejected'
     obj.save()
     return manage_farming(request)

def accept_k(request,idd):
     obj=FarmingDetails.objects.get(farming_details_id=idd)
     obj.status='accepted'
     obj.save()
     return manage_farming_krishi(request)

def reject_k(request,idd):
     obj=FarmingDetails.objects.get(farming_details_id=idd)
     obj.status='rejected'
     obj.save()
     return manage_farming_krishi(request)

