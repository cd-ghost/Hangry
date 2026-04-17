from django.contrib import admin
from .models import FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'price')
        }),
        ('Details', {
            'fields': ('description', 'image_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(FoodItem, FoodItemAdmin)
