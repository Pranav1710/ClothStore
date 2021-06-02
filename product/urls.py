from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView, ProductDeleteView, ProductUpdateView
urlpatterns = [
    path('', ProductListView.as_view() , name='home'),
    path('add/', ProductCreateView.as_view(), name='create-product' ),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='update-product' ),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='delete-product' ),
]