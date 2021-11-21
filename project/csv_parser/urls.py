from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
    path('upload/', views.upload_csv_file, name='upload'),
    path('index/<int:file_id>/', views.index, name='index'),
]
