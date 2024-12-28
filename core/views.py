from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from store.models import Product
from category.models import Category
class home(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().filter(is_available=True)[:8]
        context["category"] = Category.objects.all()
        return context
    

class CategoryBasedView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        
        if category_slug:
            cat = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.all().filter(category=cat, is_available=True)
            context["count"] = products.count()
        else:
            products = Product.objects.all().filter(is_available=True)
            context["count"] = products.count()
        
        context['category'] = Category.objects.all()
        context['products'] = products
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
        return context