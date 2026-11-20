from django.urls import path
from seed import views

urlpatterns = [
   path('seed/',views.seed),
   path('v_seed/',views.view_seed),
   path('v_seed2/',views.view_seed2),

]