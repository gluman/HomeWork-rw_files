from curses.ascii import isdigit

f = open('recipes.txt', 'r+', encoding='utf-8')

cook_book = {}


def isint(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False




for line in f:
    if isint(line) == False and ' | ' not in line and line != '\n':
        dishes = line.strip()
        cook_book[dishes] = []
    elif isint(line):
        num = int(line)
    elif ' | ' in line:
        line_dict = line.split(" | ")
        ingredient_name, quantity, measure= line_dict
        measure = measure.rstrip('\n')
        temp_dict = {'ingredient_name': ingredient_name,
                     'quantity': int(quantity),
                     'measure': measure}
        cook_book[dishes].append(temp_dict)
    elif line == '\n':
        continue

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for items in cook_book[dish]:
            for key in items:
                if res.get(items[key], False):
                    res[items[key]]['quantity'] += items['quantity']
                else:
                    if key == 'ingredient_name':
                        res[items[key]] = {'measure': items['measure'], 'quantity': items['quantity']}
    for ingredient in res:
        res[ingredient]['quantity'] *= person_count

    return res

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))




