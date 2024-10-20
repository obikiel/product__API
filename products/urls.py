from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.create_product, name='create_product'),
    path('products/get/', views.retrieve_product, name='retrieve_product'),
    path('products/<int:id>/', views.retrieve_product_by_id, name='retrieve_product_by_id'),
    path('products/update/', views.update_product, name='update_product'),
    path('products/update/<int:id>/', views.update_product_by_id, name='update_product_by_id'),
    path('products/delete/', views.delete_product, name='delete_product'),
    path('products/delete/<int:id>/', views.delete_product_by_id, name='delete_product_by_id'),
]
