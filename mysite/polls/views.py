from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Recipe, Ingredient, Allergen
from django.db import transaction
@transaction.atomic
def change_recipes(request):
    # Redirect to the admin page
    return HttpResponseRedirect(reverse('admin:index'))
@transaction.atomic
def filter_sort(request):
    # Redirect to the /polls page (or any other page you want)
    return HttpResponseRedirect(reverse('polls:index'))
@transaction.atomic
def report_view(request):
    if request.method == 'POST':
        selected_ingredients = request.POST.getlist('selected_ingredients')
        selected_allergens = request.POST.getlist('selected_allergens')
        sort_by = request.POST.get('sort_by')
        sort_order = request.POST.get('sort_order')

        # Filter recipes based on selected ingredients and allergens
        if selected_ingredients:
            recipes = Recipe.objects.filter(ingredients__id__in=selected_ingredients)
        elif selected_allergens:
            recipes = Recipe.objects.filter(allergens__id__in=selected_allergens)
        else:
            recipes = Recipe.objects.all()

        # Sort recipes based on sort_by and sort_order
        if sort_by:
            if sort_by == 'created_at':
                sort_field = 'created_at'
            else:
                sort_field = sort_by
            recipes = recipes.order_by(sort_field if sort_order == 'asc' else f'-{sort_field}')

        context = {
            'recipes': recipes,
            'selected_ingredients': selected_ingredients,
            'selected_allergens': selected_allergens,
            'sort_by': sort_by,
            'sort_order': sort_order,
        }
        return render(request, 'report_template.html', context)
    else:
        ingredients = Ingredient.objects.all()
        allergens = Allergen.objects.all()
        context = {'ingredients': ingredients, 'allergens': allergens}
        return render(request, 'report_form.html', context)
