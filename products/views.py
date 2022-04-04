from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from products.models import Product


def index(request):
    template = loader.get_template('products/index.html')
    return HttpResponse(template.render({}, request))

def product(request):
    products = Product.objects.all()
    template = loader.get_template('products/product.html')
    context = {
        'products_list': products,
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    return HttpResponse("You're looking at question %s." % product_id)
