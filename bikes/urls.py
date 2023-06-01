from django.urls import path
from . import views

urlpatterns = [
    path('', views.bikes, name='bikes'),
    path('<int:id>', views.bike_detail, name='bike_detail'),
    path('search', views.search, name='search'),
]
