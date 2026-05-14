from django.contrib import admin
from django.urls import path
from shop.views import home, catalog  # Імпортуємо твої функції з views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_url'),              # Головна сторінка (порожній шлях)
    path('catalog/', catalog, name='catalog_url'), # Сторінка каталогу
]