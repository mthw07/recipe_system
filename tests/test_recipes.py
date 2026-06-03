import pytest
from src.classes.ingredient.ingredient import Ingredient
from src.classes.recipe.recipe import Recipe
from src.classes.shopping_list.shopping_list import ShoppingList
from src.classes.dietary_recipe.dietary_recipe import DietaryRecipe

def test_ingredient_init():
    ingredient = Ingredient("Мука", 500.0, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient("Мука", 500.0, "г")
    assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_eq():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Мука", 300.0, "г")
    ingredient3 = Ingredient("Сахар", 500.0, "г")
    ingredient4 = Ingredient("Мука", 500.0, "кг")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert ingredient1 != ingredient4
