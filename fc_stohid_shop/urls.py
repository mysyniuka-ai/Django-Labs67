from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import home, catalog, product_detail, category_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_url'),
    path('catalog/', catalog, name='catalog_url'),
    path('product/<int:product_id>/', product_detail, name='product_detail_url'),
    path('category/<int:category_id>/', category_detail, name='category_detail_url'),
]

# Дозволяємо Django бачити папку media під час розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)