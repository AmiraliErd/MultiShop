from django.contrib import admin
from .models import Product, Size, Color, Information, Image


class InformationAdmin(admin.StackedInline):
    model = Information


class ImageAdmin(admin.TabularInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = (InformationAdmin, ImageAdmin)


admin.site.register(Size)
admin.site.register(Color)
