import pytest

from OOP import Ingredient, Recipe, ShoppingList


def test_init_ingredient():
    testIng = Ingredient("Мука", 500, "г")
    
    assert testIng.name == "Мука"
    assert testIng.quantity == 500.0
    assert testIng.unit == "г"

def test_str_ingredient():
    testIng = Ingredient("Мука", 500, "г")

    assert str(testIng) == "Мука: 500.0 г"

def test_eq_ingredient():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Мука", 700, "г")
    testIng3 = Ingredient("Соль", 500, "г")
    testIng4 = Ingredient("Мука", 500, "кг")

    assert testIng1 == testIng2
    assert testIng1 != testIng3
    assert testIng1 != testIng4


def test_init_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")

    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)

    assert testRecipe.title == "Странная смесь"
    assert testRecipe.ingredients == ingList


def test_add_same_ingredient_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Сахар", 700, "г")

    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    testRecipe.add_ingredient(testIng3)

    assert testRecipe.ingredients == [testIng1, Ingredient("Сахар", 1400, "г")]

def test_add_ingredient_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Соль", 700, "кг")

    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    testRecipe.add_ingredient(testIng3)

    assert testRecipe.ingredients == [testIng1, testIng2, testIng3]

def test_scale_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")


    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    scaledTestRecipe = testRecipe.scale(2)
    assert not (testRecipe is scaledTestRecipe)
    assert scaledTestRecipe.ingredients == [Ingredient("Мука", 1000, "г"), Ingredient("Сахар", 1400, "г")]
    assert scaledTestRecipe.ingredients == [Ingredient("Мука", 1000, "г"), Ingredient("Сахар", 1400, "г")]

def test_exeption_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")


    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    with pytest.raises(ValueError) as e:
        testRecipe.scale(-2.4)

def test_add_ingredient_recipe():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Сахар", 700, "г")

    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    testRecipe.add_ingredient(testIng3)

    assert len(testRecipe) == 2

def test_add_recipe_shoppinglist():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")

    ingList = [testIng1, testIng2]
    testRecipe = Recipe("Странная смесь", ingList)
    out = [(testIng1, "Странная смесь"), (testIng2, "Странная смесь")]

    testShoppingList = ShoppingList([])
    testShoppingList.add_recipe(testRecipe, 1)

    assert testShoppingList._items == out


def test_remove_recipe_shoppinglist():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Молоко", 2, "л")
    testIng4 = Ingredient("Кола", 1, "л")

    ingList1 = [testIng1, testIng2]
    ingList2 = [testIng3, testIng4]
    testRecipe1 = Recipe("Странная смесь", ingList1)
    testRecipe2 = Recipe("Странная жидкость", ingList2)
    out = [(testIng1, "Странная смесь"), (testIng2, "Странная смесь")]

    testShoppingList = ShoppingList([])
    testShoppingList.add_recipe(testRecipe1, 1)
    testShoppingList.add_recipe(testRecipe2, 1)
    testShoppingList.remove_recipe("Странная жидкость")

    assert testShoppingList._items == out


def test_list_recipe_shoppinglist():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Мука", 500, "г")
    testIng4 = Ingredient("Кола", 1, "л")

    ingList1 = [testIng1, testIng2]
    ingList2 = [testIng3, testIng4]
    testRecipe1 = Recipe("Странная смесь", ingList1)
    testRecipe2 = Recipe("Странная жидкость", ingList2)
    out = [Ingredient("Мука", 1000, "г"), Ingredient("Сахар", 700, "г"),
           Ingredient("Кола", 1, "л")]

    out.sort(key= lambda x: x.name)

    testShoppingList = ShoppingList([])
    testShoppingList.add_recipe(testRecipe1, 1)
    testShoppingList.add_recipe(testRecipe2, 1)

    assert testShoppingList.get_list() == out

def test_add_shoppinglist():
    testIng1 = Ingredient("Мука", 500, "г")
    testIng2 = Ingredient("Сахар", 700, "г")
    testIng3 = Ingredient("Мука", 500, "г")
    testIng4 = Ingredient("Кола", 1, "л")

    ingList1 = [testIng1, testIng2]
    ingList2 = [testIng3, testIng4]
    testRecipe1 = Recipe("Странная смесь", ingList1)
    testRecipe2 = Recipe("Странная жидкость", ingList2)

    testShoppingList1 = ShoppingList([])
    testShoppingList2 = ShoppingList([])

    testShoppingList1.add_recipe(testRecipe1, 1)
    testShoppingList2.add_recipe(testRecipe2, 1)

    testShoppingList3 = testShoppingList1 + testShoppingList2
    out = [Ingredient("Мука", 1000, "г"), Ingredient("Сахар", 700, "г"),
           Ingredient("Кола", 1, "л")]

    out.sort(key= lambda x: x.name)

    assert testShoppingList3.get_list() == out
    assert not (testShoppingList1 is testShoppingList3)
    assert not (testShoppingList2 is testShoppingList3)



