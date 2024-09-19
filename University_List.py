universities = [
    "Stanford University", "University of Cambridge", "University of Oxford", "MIT",
    "Yale University", "Princeton University", "University of Tokyo",
    "Columbia University", "University of Chicago", "California Institute of Technology"
]

print("Entire list:", universities)

print("6th index is", universities[6])

universities[3] = "Harvard University"
print("Updated list after changing the 4th index to 'Harvard University':", universities)

del universities[8]
print("List after deleting the 9th index:", universities)

print("Last index is", universities[-1])