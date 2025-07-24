from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'index.html', {'products': products})

def contacts(request):
    return render(request, 'contacts.html')

def woman(request):
    products = Product.objects.filter(category__title="woman", is_active=True)
    return render(request, "index.html", {'products': products})

def man(request):
    products = Product.objects.filter(category__title="man", is_active=True)
    return render(request, "index.html", {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'product_list.html', {'products': products})
