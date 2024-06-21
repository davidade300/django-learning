"""
casos os models nao estejam registrados aqui, nao e possivel fazer o CRUD
pela area administrativa do app 
"""
from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecipeAdmin)
