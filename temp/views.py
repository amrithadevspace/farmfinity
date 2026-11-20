from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'temp/home.html')
def admin(request):
    return render(request,'temp/admin.html')
def farmer(request):
    return render(request,'temp/farmer.html')
def krishibhavan(request):
    return render(request,'temp/krishibhavan.html')
def user(request):
    return render(request,'temp/user.html')


