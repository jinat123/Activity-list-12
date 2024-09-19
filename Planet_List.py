planetnames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("Entire list:", planetnames)

print("3rd index is", planetnames[3])

planetnames[6] = "Pluto"
print("Updated list after changing the 7th index to 'Pluto':", planetnames)

del planetnames[3]
print("List after deleting the 4th index:", planetnames)

print("Last index is", planetnames[-1])