from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product , Order
from .forms import ProductForm
from django.contrib.auth.models import User
# Create your views here.


@login_required
def index(request):
    
    order = Order.objects.all()
    products = Product.objects.all()
    context = {
        'orders':order,
        'products': products, 
    }
    
    return render(request, 'dashboard/index.html',context)


@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers,
        
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


# def product(request):
#     items = Product.objects.all()
#     # items = Product.objects.raw('SELECT * FROM dashboard_product ')

#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard-product')
#     else:
#         form = ProductForm()

#     context = {
#         'items': items,
#         'form': form,
#     }
#     return render(request, 'dashboard/product.html', context)



@login_required
def product(request):
    items = Product.objects.all()
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    # product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # product_name = form.cleaned_data.get('name')
            # messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/product.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


def product_update(request, pk):
    item = Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'orders': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/order.html', context)
