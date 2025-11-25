from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import permission_required
from django.contrib import messages


@permission_required('product.add_product', raise_exception=True)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('view_product_list')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})


@permission_required('product.view_product', raise_exception=True)
def view_product_list(request):
    products = Product.objects.all()
    return render(request, 'product/view_product_list.html', {'products': products})


@permission_required('product.view_product', raise_exception=True)
def view_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    return render(request, 'product/view_product.html', {'product': product})


@permission_required('product.change_product', raise_exception=True)
def edit_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if request.method == "POST":
        form = ProductForm(request.POST ,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('view_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/add_product.html', {'form': form})


@permission_required('product.delete_product', raise_exception=True)
def delete_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('view_product_list')
    return render(request, 'product/add_product.html')
