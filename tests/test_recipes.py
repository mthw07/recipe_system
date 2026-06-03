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
    with pytest.raises(ValueError):
        ingredient2 = Ingredient("Мука", -1, "г")

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

def test_recipe_init():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe = Recipe("Блюдо", [ingredient1, ingredient2])
    assert recipe.title == "Блюдо"
    assert recipe.ingredients[0] == ingredient1
    assert recipe.ingredients[1] == ingredient2

def test_recipe_add_ingredient():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe = Recipe("Блюдо", [ingredient1])
    recipe.add_ingredient(ingredient2)
    assert recipe.ingredients[1] == ingredient2
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    assert recipe.ingredients[0] == Ingredient("Мука", 1000.0, "г")
    assert recipe.ingredients[1] == ingredient2

def test_recipe_scale():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe = Recipe("Блюдо", [ingredient1, ingredient2])
    scaled_recipe = recipe.scale(2)
    assert scaled_recipe.ingredients[0] == Ingredient("Мука", 1000.0, "г")
    assert scaled_recipe.ingredients[1] == Ingredient("Сахар", 1000.0, "г")
    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_recipe_len():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe = Recipe("Блюдо", [ingredient1, ingredient2])
    assert len(recipe) == 2
    
