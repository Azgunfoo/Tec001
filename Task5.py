def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odds(test_list)
print("Original list: ", test_list)
print("Removed odd numbers: ", filtered_list)