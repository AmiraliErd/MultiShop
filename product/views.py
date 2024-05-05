from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from .models import Product, Category
from django.core.paginator import Paginator


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class CategoryStyle(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryStyle, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductsListView(ListView):
    template_name = 'product/products_list.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        request = self.request
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        queryset = Product.objects.all()
        filter_queryset = Product.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 1)
        queryset = paginator.get_page(page_number)

        if colors:
            queryset = filter_queryset.filter(color__title__in=colors).distinct()
            page_number = request.GET.get('page')
            paginator = Paginator(queryset, 1)
            queryset = paginator.get_page(page_number)
        if sizes:
            queryset = filter_queryset.filter(size__title__in=sizes).distinct()
            page_number = request.GET.get('page')
            paginator = Paginator(queryset, 1)
            queryset = paginator.get_page(page_number)
        if min_price and max_price:
            queryset = filter_queryset.filter(price__lte=max_price, price__gte=min_price)
            page_number = request.GET.get('page')
            paginator = Paginator(queryset, 1)
            queryset = paginator.get_page(page_number)

        context = super(ProductsListView, self).get_context_data()
        context['object_list'] = queryset
        return context


def search(request):
    q = request.GET.get('q')
    queryset = Product.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(queryset, 1)
    queryset = paginator.get_page(page_number)
    return render(request, 'product/products_list.html', {'object_list': queryset})


