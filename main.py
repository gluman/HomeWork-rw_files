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

