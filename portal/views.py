from django.shortcuts import render, render_to_response
from .models import Product


# Create your views here.
def home(request):
    return render(request, 'portal/home.html', {})


def my_products_list(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }
    return render(request, 'portal/my_products_list.html', context)
