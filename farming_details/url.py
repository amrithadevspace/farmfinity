from django.urls import path
from farming_details import views

urlpatterns=[
    path('p_farming_far/',views.post_farming),
    path('p_farming_kri/',views.post_farming_krishibhvan),
    path('v_farming_far/',views.view_farming),
    path('v_farming_kri/', views.view_farming_krishi),
    path('m_farming_far/',views.manage_farming),
    path('m_farming-kri/',views.manage_farming_krishi),
    path('accept/<int:idd>',views.accept),
    path('reject/<int:idd>',views.reject),
    path('accept_k/<int:idd>',views.accept),
    path('reject_k/<int:idd>',views.reject),

]