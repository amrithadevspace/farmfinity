"""
URL configuration for farmfinity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from temp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('complaint/',include('complaint.url')),
    path('farmer/',include('farmer.url')),
    path('farming_details/',include('farming_details.url')),
    path('feedback/',include('feedback.url')),
    path('fertilizer/',include('fertilizer.url')),
    path('krishibhavan/',include('krishibhavan.url')),
    path('login/',include('login.url')),
    path('notification/',include('notification.url')),
    path('order/',include('order.url')),
    path('payment/',include('payment.url')),
    path('plant/',include('plant.url')),
    path('product/',include('product.url')),
    path('seed/',include('seed.url')),
    path('service/',include('service.url')),
    path('user/',include('user.url')),
    path('temp/',include('temp.url')),
    path('forward/',include('forward.url')),
    path('',views.home),
]
