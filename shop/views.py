from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Головна сторінка
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:3]  # Беремо перші 3 товари для головної, як у тебе в коді
    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'title': 'Головна'
    })

# Каталог товарів
def catalog(request):
    items = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'catalog.html', {
        'items': items,
        'categories': categories,
        'title': 'Каталог'
    })

# Детальна сторінка товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories,
        'title': product.name
    })

# Сторінка конкретної категорії (виводить товари лише цієї категорії)
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)  # Фільтруємо товари за категорією
    categories = Category.objects.all()
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products,
        'categories': categories,
        'title': category.name
    })