def remove_all_value(value_list, remove_value):
    while remove_value in value_list:
        value_list.remove(remove_value)
    return value_list


numbers = [2, 4, 5, 6, 2, 2, 2, 2, 2, 8]
numbers_without_2 = remove_all_value(numbers, 2)
print(numbers_without_2)

animals = ['cat', 'dog', 'cat', 'cat']
animals_without_cat = remove_all_value(animals, 'cat')
print(animals_without_cat)
