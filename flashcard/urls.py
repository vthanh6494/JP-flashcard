from django.urls import path

from . import views

urlpatterns = [
    path('upload-csv/<table>/', views.csv_upload, name="csv_upload"),
    path('<table>/', views.data_all, name="list_all"),
    path('<table>/detail/', views.data_detail, name="data_detail"),
    
]