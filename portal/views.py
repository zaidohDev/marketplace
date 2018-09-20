from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def home(request):
    return render(request, 'portal/home.html', {})


def my_products_list(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }
    return render(request, 'portal/my_products_list.html', context)


def product_new(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.user = request.user
            product.name = form.cleaned_data['name']
            product.slug = form.cleaned_data['slug']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.status = 'Active'
            product.save()

            categories = Category.objects.filter(id__in=request.POST.getlist('categories'))
            if categories:
                for category in categories:
                    product.categories.add(category)

            return redirect('my_products_list')
    form = ProductForm()
    context = {
        'form': form,
            }

    return render(request, 'portal/product_new.html', context)


def product_edit(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.user != request.user:
        return HttpResponseForbidden

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.user = request.user
            product.name = form.cleaned_data['name']
            product.slug = form.cleaned_data['slug']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.save()
            return redirect('my_products_list')

    form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'portal/product_edit.html', context)
