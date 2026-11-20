from django.urls import path
from forward import views

urlpatterns=[
    path('for/<int:idd>',views.view_forward),

]