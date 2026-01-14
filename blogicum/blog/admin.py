from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_published', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'pub_date', 'is_published', 'created_at'
    )
    search_fields = ('title', 'text')
    list_filter = (
        'is_published', 'category', 'author', 'pub_date', 'created_at'
    )
