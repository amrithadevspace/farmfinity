from django.urls import path
from service import views

urlpatterns = [
   path('service/',views.service),
   path('v_service/',views.view_service),
   path('v_service2/',views.view_service2),

]