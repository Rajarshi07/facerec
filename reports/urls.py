from django.urls import path,include
import reports.views as views

urlpatterns = [
    path('', views.report),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('facedet/<str:session>/', views.facedet, name='facedet'),
]
