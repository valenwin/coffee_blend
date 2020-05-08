from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from cart.forms import CartAddProductForm
from .models import Category, Product


class BaseView(TemplateView):
    template_name = 'base.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class MenuListView(ListView):
    template_name = 'menu.html'

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        categories = Category.objects.all()
        context['products'] = products
        context['categories'] = categories
        return context


class ProductListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = Product.objects.filter(available=True)
        try:
            if self.kwargs['category_slug']:
                category = get_object_or_404(Category, slug=self.kwargs.get('category_slug'))
                products = Product.objects.filter(category=category, available=True)
                return products
        except KeyError:
            return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        categories = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context['products'] = products
        context['categories'] = categories
        context['cart_product_form'] = cart_product_form
        if self.kwargs.get('category'):
            context['category'] = get_object_or_404(Category, name=self.kwargs.get('category'))
        return context


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'products'
    template_name = 'product-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        product = get_object_or_404(self.model,
                                    slug=self.kwargs.get('slug'),
                                    available=True)
        products = Product.objects.filter(category=product.category)
        related_products = [p for p in products if p.id != product.id][:4]
        context['related_products'] = related_products
        context['product'] = product
        context['cart_product_form'] = cart_product_form
        return context
