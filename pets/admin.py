from django.contrib import admin
from .models import Pet, Category

# Register your models here.

class PetAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'gender',
        'age',
        'image'
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )

admin.site.register(Pet, PetAdmin)
admin.site.register(Category, CategoryAdmin)