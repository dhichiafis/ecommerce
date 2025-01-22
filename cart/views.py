from django.shortcuts import render,get_object_or_404,redirect
from ecom.models import Product 

from .cart import Cart 
from django.views.decorators.http import require_http_methods

from .forms import *
# Create your views here.
@require_http_methods('POST')
def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data#a variable that read the form content
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])

    return redirect('cart_detail')

def cart_detail(request):
    cart=Cart(request)
    return render(request,'cart_detail.html',{'cart':cart})
   
@require_http_methods('POST')
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
    pass

def clear_cart(request):
    cart=Cart(request)
    cart.clear()
    return redirect('product_list')