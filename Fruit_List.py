fruitnames = ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Strawberry", "Watermelon", "Cherry",
               "Blueberry", "Peach", "Pear", "Kiwi"]

print("Entire list:", fruitnames)

print("9th index is", fruitnames[9])

fruitnames[1] = "Mango"
print("Updated list after changing the 2nd index to 'Mango':", fruitnames)

del fruitnames[9]
print("List after deleting the 10th index:", fruitnames)

sliced_fruits = fruitnames[4:8]
print("Sliced portion from index 4 to 7:", sliced_fruits)

print("Last index is", fruitnames[-1])