from django.urls import path
from farmer import views

urlpatterns = [
    path('far/',views.farmer),
    path('m_far/',views.manage_farmer),
    path('accept/<int:idd>',views.accept),
    path('reject/<int:idd>',views.reject),
    path('farmersearch/', views.farmer_search),

]