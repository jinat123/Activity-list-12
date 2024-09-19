worldcurrencies = [
    "US Dollar", "British Pound", "Japanese Yen", "Indian Rupee", "Canadian Dollar",
    "Australian Dollar", "Swiss Franc", "Chinese Yuan", "South Korean Won", "Russian Ruble"
]

print("Entire list:", worldcurrencies)

print("4th index is", worldcurrencies[4])

worldcurrencies[6] = "Euro"
print("Updated list after changing the 7th index to 'Euro':", worldcurrencies)

del worldcurrencies[8]
print("List after deleting the 9th index:", worldcurrencies)

print("Last index is", worldcurrencies[-1])