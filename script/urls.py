from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('script/', views.script_data, name='script_data'),
]
