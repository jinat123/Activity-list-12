countriesandcontinents = [
    ("United States", "North America"), ("Canada", "North America"), ("Brazil", "South America"),
    ("Germany", "Europe"), ("India", "Asia"), ("South Africa", "Africa"), ("China", "Asia"),
    ("Russia", "Europe"), ("Egypt", "Africa"), ("Japan", "Asia"), ("Australia", "Oceania"),
    ("Argentina", "South America"), ("France", "Europe"), ("Nigeria", "Africa"), ("Mexico", "North America")
]

print("Entire list:", countriesandcontinents)

print("9th index is", countriesandcontinents[9])

countriesandcontinents[9] = ("Australia", "Oceania")
print("Updated list after changing the 10th index to 'Australia':", countriesandcontinents)

del countriesandcontinents[11]
print("List after deleting the 12th index:", countriesandcontinents)

sliced_countries = countriesandcontinents[4:9]
print("Sliced portion from index 4 to 8:", sliced_countries)

print("Last index is", countriesandcontinents[-1])