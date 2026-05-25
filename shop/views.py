from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# ВИПРАВЛЕНО: Прибрали нерозподілений імпорт 'Review', який підсвічувався жовтим
from .models import Category, Product, Order
from .forms import SubscriptionForm, ReviewForm


# Головна сторінка
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:3]

    if request.method == 'POST':
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('home_url')
    else:
        sub_form = SubscriptionForm()

    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'title': 'Головна',
        'sub_form': sub_form
    })


# Каталог товарів
def catalog(request):
    items = Product.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('catalog_url')
    else:
        sub_form = SubscriptionForm()

    return render(request, 'catalog.html', {
        'items': items,
        'categories': categories,
        'title': 'Каталог',
        'sub_form': sub_form
    })


# Детальна сторінка товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    reviews = product.reviews.all()

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if average_rating:
        average_rating = round(average_rating, 1)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.product = product
            new_review.save()
            return redirect('product_detail_url', product_id=product.id)
    else:
        review_form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories,
        'title': product.name,
        'reviews': reviews,
        'average_rating': average_rating,
        'review_form': review_form
    })


# Сторінка конкретної категорії
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'category_detail.html', {
        'category': category,
        'products': products,
        'categories': categories,
        'title': category.name
    })


# --- ЛАБА 8: АВТЕНТИФІКАЦІЯ ТА ПРОФІЛЬ ---

# Реєстрація
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    # ВИПРАВЛЕНО: Прибрали префікс 'auth/', так як файл лежить прямо в templates
    return render(request, 'register.html', {'form': form, 'title': 'Реєстрація'})


# Вихід з акаунта
def logout_view(request):
    logout(request)
    return redirect('home_url')


# Особистий кабінет
@login_required(login_url='login_url')
def profile_view(request):
    categories = Category.objects.all()

    if request.user.is_staff:
        orders = Order.objects.all().order_by('-created_at')
        role = "Адміністратор"
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        role = "Покупець"

    # ВИПРАВЛЕНО: Прибрали префікс 'auth/', так як файл лежить прямо в templates
    return render(request, 'profile.html', {
        'orders': orders,
        'role': role,
        'categories': categories,
        'title': 'Особистий кабінет'
    })