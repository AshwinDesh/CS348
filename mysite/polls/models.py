from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    allergens = models.ManyToManyField('Allergen', through='RecipeAllergen')
    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200, db_index=True)
    calories = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return self.ingredient_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    def __str__(self):
        return self.recipe.recipe_name

class Allergen(models.Model):
    allergen_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.allergen_name

class RecipeAllergen(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    def __str__(self):
        return self.recipe.recipe_name

