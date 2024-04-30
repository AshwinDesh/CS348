# Generated by Django 5.0.4 on 2024-04-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_allergen_ingredient_recipe_recipeallergen_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="allergens",
            field=models.ManyToManyField(
                through="polls.RecipeAllergen", to="polls.allergen"
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                through="polls.RecipeIngredient", to="polls.ingredient"
            ),
        ),
    ]