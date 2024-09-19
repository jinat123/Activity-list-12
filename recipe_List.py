recipes = [
    "Spaghetti Bolognese", "Chicken Curry", "Beef Stroganoff", "Tacos", "Pancakes",
    "Caesar Salad", "Fried Rice", "Grilled Cheese", "Lasagna", "Burritos",
    "Sushi", "Ratatouille", "Quiche", "Paella", "Chocolate Cake"
]

print("Entire list:", recipes)

print("12th index is", recipes[12])

recipes[8] = "Lasagna"
print("Updated list after changing the 9th index to 'Lasagna':", recipes)

del recipes[10]
print("List after deleting the 11th index:", recipes)

sliced_recipes = recipes[5:11]
print("Sliced portion from index 5 to 10:", sliced_recipes)

print("Last index is", recipes[-1])