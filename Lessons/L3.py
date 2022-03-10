def remove_all_occurences(original_list, remove_value):
    new_list = original_list.copy()
    for value_checking in original_list:
        if value_checking == remove_value:
            new_list.remove(value_checking)
    return new_list


def remove_all_items(l, item_to_remove):
    occurences = 0
    for item in l:
        if item == item_to_remove:
            occurences = occurences + 1
    for i in range(occurences):
        l.remove(item_to_remove)
    return l
    
 
        
        
numbers = [2, 4, 5, 6, 2, 2, 2, 2, 2, 8]
numbers_without_2 = remove_all_occurences(numbers, 2)
print(numbers_without_2)
numbers_without_2 = remove_all_items(numbers, 2)
print(numbers_without_2)

letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'c', 'c']
letters_without_a = remove_all_occurences(letters, 'a')
print(letters_without_a)
letters_without_a = remove_all_items(letters, 'a')
print(letters_without_a)

animals = ['cats', 'dogs', 'dogs', 'cats']
animals_without_cats = remove_all_occurences(animals, 'cats')
print(animals_without_cats)
animals_without_cats = remove_all_items(animals, 'cats')
print(animals_without_cats)

