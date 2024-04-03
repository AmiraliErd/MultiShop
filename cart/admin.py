from django.contrib import admin
from .models import Order, OrderItem, DiscountCode


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (OrderItemAdmin,)
    list_filter = ('is_paid',)


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'discount')


