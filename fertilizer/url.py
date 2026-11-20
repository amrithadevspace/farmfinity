from django.urls import path
from fertilizer import  views

urlpatterns = [
    path('ferti/',views.fertilizer),
    path('v_ferti/',views.view_fertilizer),

]