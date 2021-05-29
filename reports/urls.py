from django.urls import path,include,re_path
import reports.views as views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index),
    path('facedet/<str:session>/', views.facedet, name='facedet'),
    path('facedet_alt/<str:session>/', views.facedet_alt, name='facedet'),
    path('reports/', views.reports, name='reports'),
    re_path(r'^webcam.js', (TemplateView.as_view(template_name="webcam.js", content_type='application/javascript', )), name='webcam.js'),
]
