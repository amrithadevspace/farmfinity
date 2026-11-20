from django.urls import path
from order import views


urlpatterns=[
    path('order/<int:idd>',views.order),
    path('v_order/',views.manage_order),
    path('v_order2/', views.view_order2),
    path('v_history/',views.view_history),
    path('accept_o/<int:idd>',views.accept),
    path('reject_o/<int:idd>',views.reject),


]