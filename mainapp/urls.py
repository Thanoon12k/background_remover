from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('process/', views.ProcessImage, name='process_image'),
    path('download/', views.DownloadImage, name='download_image'),
]
