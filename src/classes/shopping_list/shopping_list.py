from src.classes.ingredient.ingredient import Ingredient
from src.classes.recipe.recipe import Recipe

class ShoppingList:
    def __init__(self, _items: list[tuple[Ingredient, str]]):
        self._items = _items

    def add_recipe(self, recipe: Recipe, portions: float):
        if(portions <= 0):
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        for i in range(len(self._items), 0, -1):
            if(self._items[i-1][1] == title):
                self._items.pop(i-1)

    def get_list(self):
        dict_of_ingredients = dict()
        for item in self._items:
            if((item[0].name, item[0].unit) in dict_of_ingredients):
                dict_of_ingredients[(item[0].name, item[0].unit)] += item[0].quantity
            else:
                dict_of_ingredients[(item[0].name, item[0].unit)] = (item[0].quantity)
        
        list_of_ingredients = []
        for ingredient in dict_of_ingredients:
            list_of_ingredients.append(Ingredient(ingredient[0], dict_of_ingredients[ingredient], ingredient[1]))
        
        list_of_ingredients.sort(key=lambda x: x.name)
        
        return list_of_ingredients
    
    def __add__(self, other: ShoppingList):
        new_items = self._items + other._items
        return ShoppingList(new_items)
    