# from django.contrib import admin

# from .models import Recipe,Ingredient,Allergen,RecipeAllergen,RecipeIngredient

# admin.site.register(Recipe)
# admin.site.register(Ingredient)
# admin.site.register(Allergen)
# admin.site.register(RecipeAllergen)
# admin.site.register(RecipeIngredient)
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeAllergen, Allergen

def generate_report(modeladmin, request, queryset):
    # Your report generation logic here
    selected_recipes = list(queryset)
    # Generate and display the report based on selected_recipes
    # This can be a CSV file, PDF, or HTML report

generate_report.short_description = "Generate Report"

class IngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class AllergenInline(admin.TabularInline):
    model = RecipeAllergen
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    inlines += [AllergenInline]
    actions = [generate_report]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Allergen)
#admin.site.register(RecipeAllergen)
admin.site.register(Ingredient)
#admin.site.register(RecipeIngredient)
