famousvolcanoes = [
    "Mount Fuji", "Mount Etna", "Krakatoa", "Mauna Loa", "Mount St. Helens", "Mount Kilimanjaro", "Mount Vesuvius"
]

print("Entire list:", famousvolcanoes)

print("4th index is", famousvolcanoes[4])

famousvolcanoes[2] = "Mount Vesuvius"
print("Updated list after changing the 3rd index to 'Mount Vesuvius':", famousvolcanoes)

del famousvolcanoes[4]
print("List after deleting the 5th index:", famousvolcanoes)

print("Last index is", famousvolcanoes[-1])