from django.shortcuts import render, get_object_or_404
from .models import Product,Cart
# Create your views here.
def product(request , item_id):
    top_price = Product.objects.order_by('-price')[:10]
    items = get_object_or_404(Product, id=item_id)
    all = {
        'price':top_price,
        'items' :items,
    }
    return render(request , 'product_detail.html' , all )

def product_overview(request):
    top_price = Product.objects.order_by('-price')[:10]
    return render(request,'product_overview.html',{'product':top_price})

def cart(request):
    items = Cart.objects.all()
    return render(request,'cart.html',{"items":items})