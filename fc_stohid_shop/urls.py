from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import home, catalog, product_detail, category_detail, register_view, logout_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Адмін-панель
    path('admin/', admin.site.urls),

    # Основні сторінки магазину
    path('', home, name='home_url'),
    path('catalog/', catalog, name='catalog_url'),
    path('product/<int:product_id>/', product_detail, name='product_detail_url'),
    path('category/<int:category_id>/', category_detail, name='category_detail_url'),

    # ЛАБА 8: Авторизація, реєстрація та кабінет (шаблони шукаються прямо в папці templates)
    path('register/', register_view, name='register_url'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('profile/', profile_view, name='profile_url'),

    # Відновлення пароля (Email-посилання генеруються в термінал PyCharm)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]

# Робота з медіа-файлами (картинками товарів) під час розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)