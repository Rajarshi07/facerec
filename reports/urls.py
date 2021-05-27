from django.urls import path,include,re_path
import reports.views as views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.report),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('facedet/<str:session>/', views.facedet, name='facedet'),
    re_path(r'^/static/fapi/dist/face-api.esm.js', (TemplateView.as_view(template_name="/static/fapi/dist/face-api.esm.js", content_type='application/javascript', )), name='/static/fapi/dist/face-api.esm.js'),
]
