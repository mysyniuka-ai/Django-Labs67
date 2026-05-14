from django.shortcuts import render
from .models import Category, Product


def home(request):
    # Отримуємо всі категорії та всі товари з бази даних
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'title': 'Офіційний магазин ФК Стохід',
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)


def catalog(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'products': products})