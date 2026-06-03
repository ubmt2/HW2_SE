from typing import List


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, value: float) -> None:
        if value > 0:
            self._quantity = float(value)
        else:
            raise ValueError("Количество должно быть положительным")

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if isinstance(other, Ingredient) and self.name == other.name and \
                self.unit == other.unit:
            return True

        return False


class Recipe:
    def __init__(self, title: str, ingredients: List[Ingredient]) -> None:
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient) -> None:
        if ingredient in self.ingredients:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio: int | float) -> bool:
        return ratio > 0

    def scale(self, ratio: float):
        output = Recipe(self.title, [])
        for i in self.ingredients:
            i.quantity *= ratio
            output.add_ingredient(i)

        return output

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        output = f"{self.title}:\n"

        for i in self.ingredients:
            output += str(i) + "\n"

        return output


class ShoppingList:
    def __init__(self, items: List[tuple[Ingredient, str]]) -> None:
        self._items = items

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if not Recipe.is_valid_ratio(portions):
            raise ValueError("Количество порций должно быть положительным")

        for i in recipe.scale(portions):
            self._items.append((i, recipe.title))

    def remove_recipe(self, title: str) -> None:
        self._items = list(filter(lambda x: x[1] != title, self._items))

    def get_list(self) -> dict:
        dictOfIngredients = dict()

        for ing, recipe in self._items:
            key = (ing.name, ing.unit)
            if key in dictOfIngredients:
                dictOfIngredients[key] += ing.quantity
            else:
                dictOfIngredients[key] = ing.quantity

        output = []

        for name, unit, quantity in dictOfIngredients.items():
            output.append(Ingredient(name, quantity, unit))

        output.sort(key=lambda x: x.name)

        return output

    def __add__(self, other):
        if not isinstance(other, ShoppingList):
            raise ValueError("Складывать можно только списки покупок")
        newList = self._items
        newList.extend(other._item)

        return ShoppingList(newList)


class DiataryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=[] | List[Ingredient]) -> None:
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        newList = self.super().scale(ratio).ingredients

        return DiataryRecipe(self.title, self.diet_type, newList)

    def __str__(self) -> str:
        output = super().__str__()

        return f"[{self.diet_type}] {output}"