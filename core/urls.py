from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('register_ip', views.register_ip, name='register_ip'),
    path('search_ip', views.search_ip, name='search_ip'),
    path('edit_ip/<int:mac_id>/', views.edit_ip, name='edit_ip'), 
    
]