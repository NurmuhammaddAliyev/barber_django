from django.contrib import admin
from .models import User, ServiceCategory, Service, Barber


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role')
    search_fields = ('name', 'email')
    list_filter = ('role',)


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('is_active',)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'category')
