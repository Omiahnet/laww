from django.urls import path
from cases import views
 


app_name = 'cases'

urlpatterns = [
    path('', views.index, name='index'),       
 
]