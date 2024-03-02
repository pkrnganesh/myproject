from django.urls import path
from . import views


#url conf
urlpatterns = [
    path('', views.index, name = 'index')
]