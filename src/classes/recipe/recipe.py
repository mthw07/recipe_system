from src.classes.ingredient.ingredient import Ingredient
    
class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        for one_ingredient in self.ingredients:
            if(one_ingredient == ingredient):
                one_ingredient.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        if ((type(ratio) == int or type(ratio) == float) and ratio > 0):
            return True
        return False
        
    def scale(self, ratio:float):
        if(not self.is_valid_ratio(ratio)):
            raise ValueError("Коэффициент должен быть положительным")
        else:
            new_ingredients = []
            for ingredient in self.ingredients:
                new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
                new_ingredients.append(new_ingredient)
            return Recipe(self.title, new_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        output = f"Название блюда: {self.title}\n"
        output += "Необходимые ингредиенты:\n"
        for ingredient in self.ingredients:
            output += f"• {str(ingredient)}\n"
        return output