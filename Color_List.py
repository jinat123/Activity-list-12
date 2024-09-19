colornames = ["Red", "Blue", "Green", "Yellow", "Orange", "Pink", "Brown", "Black", "White", "Gray",
               "Violet", "Indigo", "Cyan", "Magenta", "Lime"]

print("Entire list:", colornames)

print("10th index is", colornames[10])

colornames[3] = "Purple"
print("Updated list after changing the 4th index to 'Purple':", colornames)

del colornames[4]
print("List after deleting the 5th index:", colornames)

sliced_colors = colornames[2:9]
print("Sliced portion from index 2 to 8:", sliced_colors)

print("Last index is", colornames[-1])