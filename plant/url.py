from django.urls import path
from plant import views

urlpatterns = [
    path('plant/',views.plant),
    path('v_plant/',views.view_plant),
    path('v_plant2/', views.view_plant2),

]