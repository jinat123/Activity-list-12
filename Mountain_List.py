mountainnames = [
    "K2", "Kangchenjunga", "Denali", "Aconcagua", "Mont Blanc", "Matterhorn", "Mount Kilimanjaro", "Mount Elbrus"
]

print("Entire list:", mountainnames)

print("5th index is", mountainnames[5])

mountainnames[2] = "Everest"
print("Updated list after changing the 3rd index to 'Everest':", mountainnames)

del mountainnames[5]
print("List after deleting the 6th index:", mountainnames)

print("Last index is", mountainnames[-1])