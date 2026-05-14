from django.contrib import admin
from .models import Category, Product, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # ВИПРАВЛЕНО: було admin.admin.ModelAdmin
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # ВИПРАВЛЕНО
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):  # ВИПРАВЛЕНО
    list_display = ('author', 'product', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)