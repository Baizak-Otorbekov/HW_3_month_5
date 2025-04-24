from django.contrib import admin
from apps.product.models import Product, ProductImage, Category
from django.utils.html import format_html

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px"/>', obj.image.url)
        
    image_tag.short_description = 'Изображение'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'image_tag')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')

    inlines = [ProductImageAdmin]

    def image_tag(self, obj):
        first_image = obj.get_first_image()
        if first_image:
            return format_html('<img src="{}" width="auto" height="50px"/>', first_image)
        return "-"
        
    image_tag.short_description = 'Изображение'