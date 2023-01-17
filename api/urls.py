from unicodedata import name
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('api_map/<int:zip_code>/', views.api_map, name='api_map' ),
    path('api_ppe',                 views.api_ppe, name='api_ppe')
]