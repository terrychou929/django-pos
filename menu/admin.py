from django.contrib import admin
from .models import MenuItem, Ingredient, MenuItemIngredient

class MenuItemIngredientInline(admin.TabularInline):
    model = MenuItemIngredient
    extra = 1

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    inlines = [MenuItemIngredientInline]
    search_fields = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit')
    search_fields = ('name',)

@admin.register(MenuItemIngredient)
class MenuItemIngredientAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity')