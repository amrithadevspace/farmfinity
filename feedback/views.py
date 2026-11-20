from django.shortcuts import render
from feedback.models import Feedback
import datetime

# Create your views here.
def feedback (request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Feedback()
        obj.user_id=ss
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.type='user'
        obj.save()
    return render(request,'feedback/post feedback.html')

def view_feedback(request):

    obj=Feedback.objects.filter(type='user')
    context={
        'aa':obj
    }
    return render(request,'feedback/view feedback.html',context)


def feedback_f (request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Feedback()
        obj.farmer_id=ss
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.type='farmer'
        obj.save()
    return render(request,'feedback/post feedback_f.html')

def view_feedback_f(request):
    obj=Feedback.objects.filter(type='farmer')
    context={
        'aa':obj
    }
    return render(request,'feedback/view feedback_f.html',context)