from django.contrib import admin
from .models import Post, Category, Tags, Sale

admin.site.register(Category)
admin.site.register(Tags)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish')


admin.site.register(Post, PostAdmin )


class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'cost', 'category', 'publish', 'author')


admin.site.register(Sale, SaleAdmin)