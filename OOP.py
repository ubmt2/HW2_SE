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