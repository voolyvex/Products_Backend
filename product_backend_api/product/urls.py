from django.urls import path
from . import views

urlpatterns = [
    path('product_backend_api/', views.products_list),
    path('<int:pk>/', views.product_detail),
]