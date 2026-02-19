from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_form, name='api_form'),
    path('my-api/', views.my_api, name='my_api'),
    path('api/products/',views.product_list,name='product_list'),
    path('products-ui/', views.product_ui, name='product_ui'),
]
