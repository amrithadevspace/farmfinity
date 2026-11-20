from django.urls import path
from temp import views

urlpatterns=[
    path('home/',views.home),
    path('admin/',views.admin),
    path('krishibhavan/',views.krishibhavan),
    path('farmer/',views.farmer),
    path('user/',views.user),



]