import pprint
cook_book = {}
with open('recipes.txt', encoding="utf8") as f:
    for line in f:
        dish_name = line.strip()
        num_ingredients = int(f.readline().strip())
        ingridient_list = []
        for ingridient in range(num_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            ingridient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingridient_list.append(ingridient_dict)
        cook_book.setdefault(dish_name, ingridient_list)
        separate = f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    dicе_with_shopping_list = {}
    for dishes_name in dishes:
        ingridients_list = cook_book.get(dishes_name)
        for i in ingridients_list:
            name_ingridient, measure_name, quantity_1 = i.get('ingredient_name'), i.get('measure'), i.get('quantity')
            ingridient_key = {'measure': measure_name, 'quantity': quantity_1}
            dicе_with_shopping_list.setdefault(name_ingridient, ingridient_key)
    return print(dicе_with_shopping_list)
get_shop_list_by_dishes(['Запеченный картофель'], 2)