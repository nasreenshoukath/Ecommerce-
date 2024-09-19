from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Category
from django.contrib import messages

# Create your views here.




def home(request):
    product = Product.objects.all()
    return render(request,'home/index.html',{'products': product})

def add_product(request):
    categories = Category.objects.all()
    if request.method =='POST':
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        prod_image = request.FILES.get('product_image')
        category = request.POST.get('product_category')
        my_category = get_object_or_404(Category, id = category)
        Product.objects.create(name = name, description = description, product_image = prod_image, category = my_category)

        messages.success(request, 'Product Added Sucessfully')
        return redirect('home')
    return render(request,'home/add_product.html',{'categories':categories})

def edit_product(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('product_name')
        product.description = request.POST.get('product_description')
        product_image = request.FILES.get('product_image')
        if product_image:
            product.product_image = product_image
        category_id = request.POST.get('product_category')
        product.category = get_object_or_404(Category, id = category_id)
        product.save()
        messages.success(request, 'Product updated Sucessfully')
        return redirect('home')

    return render(request,'home/edit_product.html',{'product' : product,'categories': categories})
def delete_product(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product Deleted Sucessfully')
        return redirect('home')
    return render(request,'home/confirm_deletion.html',{'product' : product})