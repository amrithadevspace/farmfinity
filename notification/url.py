from django.urls import path
from notification  import views


urlpatterns = [
    path('notifi/',views.notification),
    path('v_notify/',views.view_notification),
    path('v_notify2/',views.view_notification2),


    ]