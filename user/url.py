from django.urls import path
from user import views


urlpatterns=[
    path('user/',views.user),
    path('v_user/',views.view_user),

]