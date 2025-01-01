from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View
from .models import CartItem
from store.models import Product,Variation
from decimal import Decimal
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class cartView(LoginRequiredMixin,TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(user=self.request.user)
        total_price = sum(item.quantity * item.product.price for item in cart_items)
        tax = round(total_price * Decimal(0.05),2)
        grand_total = total_price + tax
        context['cart_items'] = cart_items
        context['cart_item_count'] = cart_items.count()
        context['tax'] = tax
        context['grand_total'] = grand_total
        context['total_price'] = total_price
        context["category"] = Category.objects.all()
        return context
    
@login_required  
def add_to_cart(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        color = request.POST['color']
        size = request.POST['size']
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user,color=color,size=size)
        cart_item.quantity += 1
        cart_item.product.stock=cart_item.product.stock-1
        cart_item.product.save()
        cart_item.save()
        return redirect('cart')
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem,id=product_id)
    cart_item.product.stock=cart_item.product.stock+cart_item.quantity
    cart_item.product.save()
    cart_item.delete()
    return redirect('cart')

@login_required
def increment(request,id):
    cart_item = get_object_or_404(CartItem,id=id)
    if cart_item.product.stock > 0:
        cart_item.product.stock=cart_item.product.stock-1
        cart_item.product.save()
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def decrement(request,id):
    cart_item = get_object_or_404(CartItem,id=id)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.product.stock=cart_item.product.stock+1
        cart_item.product.save()
        cart_item.save()

    return redirect('cart')
