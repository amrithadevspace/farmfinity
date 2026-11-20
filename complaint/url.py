from django.urls import path
from complaint import views


urlpatterns=[
    path('com/',views.complaint),
    path('v_com/',views.view_complaint),
    path('rep/<int:idd>',views.post_reply),
    path('v_rep/',views.view_reply),
    path('f_com/',views.farmer_complaint),
    path('v_fcom/',views.view_farmer_complaint),
    path('v_fcom2/',views.view_farmer_complaint2),
    path('f_rep/<int:idd>',views.farmer_reply),
    path('v_frep/',views.view_farmer_reply),
    path('com2/',views.complaint2),
    path('v_com2/',views.view_complaint2),
    path('rep2/<int:idd>',views.post_reply2),
    path('v_rep2/',views.view_reply2),




]