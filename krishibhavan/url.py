from django.urls import path
from krishibhavan import views

urlpatterns=[
    path('krishi/',views.krishibhavan),
    path('v_krishi/',views.view_krishibhavan),
    path('k_search/',views.krishibhavan_search),

]