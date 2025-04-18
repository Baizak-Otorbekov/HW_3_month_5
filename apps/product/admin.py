from django.contrib import admin
from apps.product.  models import Product, ProductImage 
from django.utils.html import format_html

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px"/>', format(obj.image.
            url))
        
    image_tag.short_description = 'Изображение'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'image_tag')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('price',)

    inlines = [ProductImageAdmin]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px"/>', obj.get_first_image().url)
        
    image_tag.short_description = 'Изображение'