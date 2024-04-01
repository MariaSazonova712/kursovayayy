from django.contrib import admin
from .models import Task, Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'owner', 'task', 'phone', 'description')
    list_display_links = ('id', 'created', 'owner', 'task', 'phone', 'description')


@admin.register(Task)
class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'price', 'square')
    list_display_links = ('id', 'name', 'place', 'price', 'square')
