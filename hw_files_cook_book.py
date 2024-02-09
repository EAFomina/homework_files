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

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_for_list = cook_book()
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book_for_list.get(dish)
        for ingredient in ingredients:
            ingredient_name = ingredient.get('ingredient_name')
            measure = ingredient.get('measure')
            quantity = ingredient.get('quantity') * person_count
            if ingredient_name in shop_list:
                first_quantity = (shop_list.get(ingredient_name)).get('quantity')
                shop_list[ingredient_name] = {'measure': measure, 'quantity': first_quantity + quantity}
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Пюре'], 2)