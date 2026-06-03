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
    
def test_shopping_list_add_recipe():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe = Recipe("Блюдо", [ingredient1, ingredient2])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 1)
    assert shopping_list.get_list()[0] == ingredient1
    assert shopping_list.get_list()[1] == ingredient2
    shopping_list.add_recipe(recipe, 2)
    assert shopping_list.get_list()[0] == Ingredient("Мука", 1500.0, "г")
    assert shopping_list.get_list()[1] == Ingredient("Сахар", 1500.0, "г")
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, -1)

def test_shopping_list_remove_recipe():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    recipe1 = Recipe("Блюдо", [ingredient1, ingredient2])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1, 1)
    shopping_list.remove_recipe("Блюдо")
    assert len(shopping_list.get_list()) == 0
    shopping_list.add_recipe(recipe1, 1)
    shopping_list.remove_recipe("Несуществующее Блюдо")
    assert len(shopping_list.get_list()) == 2

def test_shopping_list_get_list():
    ingredient1 = Ingredient("Амука", 500.0, "г")
    ingredient2 = Ingredient("Бсахар", 500.0, "г")
    recipe1 = Recipe("Блюдо 1", [ingredient1, ingredient2])
    recipe2 = Recipe("Блюдо 2", [ingredient1])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe1, 1)
    shopping_list.add_recipe(recipe2, 1)
    ingredients = shopping_list.get_list()
    assert len(ingredients) == 2
    assert ingredients[0] == Ingredient("Амука", 1000.0, "г")
    assert ingredients[1] == Ingredient("Бсахар", 500.0, "г")

def test_shopping_list_add():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Сахар", 500.0, "г")
    shopping_list1 = ShoppingList()
    shopping_list2 = ShoppingList()
    shopping_list1.add_recipe(Recipe("Блюдо 1", [ingredient1]), 1)
    shopping_list2.add_recipe(Recipe("Блюдо 2", [ingredient2]), 1)
    combined_list = shopping_list1 + shopping_list2
    assert len(combined_list.get_list()) == 2
    assert combined_list.get_list()[0] == ingredient1
    assert combined_list.get_list()[1] == ingredient2
    assert shopping_list1.get_list()[0] == ingredient1
    assert shopping_list2.get_list()[0] == ingredient2
    