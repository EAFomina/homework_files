def cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f.read().split('\n\n'):
            dish_name, ingredient_number, *ingredients = line.split('\n')
            dish_list = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ingredient.split(' | '))
                dish_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = dish_list
    return cook_book