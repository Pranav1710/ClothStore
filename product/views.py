from product.models import Product
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'quantity', 'price']
    success_url = "/product/"
    
    def form_valid(self, form: Product):
        return super().form_valid(form)
    
  
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'quantity', 'price']
    success_url = "/product/"
    
    def form_valid(self, form: Product):
        return super().form_valid(form)
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = "/product/"
    