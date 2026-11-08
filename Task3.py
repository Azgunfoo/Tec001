cities = []
print("Enter 5 cities name:")
for i in range(5):
    city = input(f"City {i + 1}: ")
    cities.append(city)
print("\nYour city")
for city in cities:
    print(city)
def sum_of_list(numbers):
    return sum(numbers)
test_list = [10, 20, 30, 40, 50]
result = sum_of_list(test_list)
print("Original list:", test_list)
print("All the numbers:", result)