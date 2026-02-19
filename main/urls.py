from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_form, name='api_form'),
    path('my-api/', views.my_api, name='my_api'),
]
