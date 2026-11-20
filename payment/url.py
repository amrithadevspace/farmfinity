from django.urls import path
from payment import views

urlpatterns = [
    path('pay/<int:idd>',views.payment),
    path('v_pay/',views.view_payment),


]