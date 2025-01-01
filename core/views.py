from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,DetailView,ListView
from store.models import Product
from category.models import Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.models import CartItem
class home(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().filter(is_available=True)[:8]
        context["category"] = Category.objects.all()
        context['cart_item_count'] = CartItem.objects.filter(user=self.request.user).count()
        return context
    

class CategoryBasedView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        
        if category_slug:
            cat = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.all().filter(category=cat, is_available=True).order_by('created_date')
            context["count"] = products.count()
            paginator = Paginator(products, 6)
            page = self.request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
        else:
            products = Product.objects.all().filter(is_available=True)
            context["count"] = products.count()
            paginator = Paginator(products, 6)
            page = self.request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
 
        context['category'] = Category.objects.all()
        context['products'] = products
        context['cart_item_count'] = CartItem.objects.filter(user=self.request.user).count()
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        product_slug = self.kwargs.get('product_slug')
        return get_object_or_404(Product, slug=product_slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context['cart_item_count'] = CartItem.objects.filter(user=self.request.user).count()
        return context
    
class SearchView(ListView):
    model=Product
    template_name='store.html'
    context_object_name='products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword=self.request.GET.get('keyword')
        if keyword:
            products=Product.objects.filter(product_name__icontains=keyword)
            context["count"]=products.count()
            
        else:
            products={} 
            context["count"]=0

        context["products"]=products
        context["category"]=Category.objects.all()
        context['cart_item_count'] = CartItem.objects.filter(user=self.request.user).count()
        return context
   
    
    
