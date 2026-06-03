from src.classes.recipe.recipe import Recipe
        
class DietaryRecipe(Recipe):
        
    def __init__(self, title: str, diet_type: str, ingredients = None):
        if(ingredients is None):
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type
        
    def scale(self, ratio):
        simple_recipe = super().scale(ratio)
        return DietaryRecipe(simple_recipe.title, self.diet_type, simple_recipe.ingredients)
            
    def __str__(self):
        output = f"Название блюда: [{self.diet_type}] {self.title}\n"
        output += "Необходимые ингредиенты:\n"
        for ingredient in self.ingredients:
            output += f"• {str(ingredient)}\n"
        return output