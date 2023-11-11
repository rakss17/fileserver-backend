from django.urls import path
from . import views

urlpatterns = [
    path('file_list/', views.file_list, name='file_list'), 
     path('file_list/delete/<int:file_id>/', views.delete_file, name='delete_file'),
]
