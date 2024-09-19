continents = [
    "Asia", "Europe", "North America", "South America", "Antarctica", "Africa", "Australia"
]

print("Entire list:", continents)

print("4th index is", continents[4])

continents[1] = "Africa"
print("Updated list after changing the 2nd index to 'Africa':", continents)

del continents[5]
print("List after deleting the 6th index:", continents)

print("Last index is", continents[-1])