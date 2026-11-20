from django.urls import path
from feedback import views

urlpatterns = [
    path('feed/',views.feedback),
    path('v_feed/',views.view_feedback),
    path('feed_f/',views.feedback_f),
    path('v_feed_f/',views.view_feedback_f),

]