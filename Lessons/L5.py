def remove_all_occurences(original_list, remove_value):
    new_list = original_list.copy()
    for value_checking in original_list:
        if value_checking == remove_value:
            new_list.remove(value_checking)
    return new_list


numbers = [2, 4, 5, 6, 2, 2, 2, 2, 2, 8]
numbers_without_2 = remove_all_occurences(numbers, 2)
print(numbers_without_2)

# ------


numbers = [2, 4, 5, 6, 2, 2, 2, 2, 2, 8]
numbers_without_2 = list(filter((2).__ne__, numbers))
print(numbers_without_2)
