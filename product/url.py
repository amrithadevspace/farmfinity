from django.urls import path
from product import views
from product.views import ProductList

urlpatterns = [
    path('prod/',views.product),
    path('v_prod/',views.view_product),
    path('productsearch/', views.product_search),
    path('v_prod2/', views.view_product2),
    path('update/<int:idd>',views.update),
    path('v_update/',views.view_update),
    path('view_reply/<int:idd>',views.view_update),
    path('wishlist/<int:idd>',views.addto_wishlist),
    path('v_wishlist/',views.view_wishlist),
    path('remove_wishlist/<int:idd>/', views.remove_wishlist),
    path('prodApI/',ProductList.as_view()),
    path('postAPI',ProductList.as_view()),
    path('putAPI/<int:id>/',ProductList.as_view()),
    path('patchAPI/<int:id>/', ProductList.as_view()),
    path('deleteAPI/<int:id>/', ProductList.as_view()),




]