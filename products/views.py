from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from reviews.forms import ReviewForm
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {'products': products})    
    
def product_item(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ReviewForm()
    return render(request, "products/product_item.html", {'product': product, 'review_form': form })

def search_products(request):
    match = request.GET.get('match')
    
    products = Product.objects.filter(name__icontains=request.GET['query'])
    
    return render(request, "products/product_list.html", {"products": products})