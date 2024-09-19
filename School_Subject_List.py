schoolsubjects = [
    "English", "History", "Geography", "Physics", "Chemistry", "Biology", "Physical Education",
    "Art", "Music", "Computer Science", "Economics", "Psychology"
]

print("Entire list:", schoolsubjects)

print("6th index is", schoolsubjects[6])

schoolsubjects[7] = "Mathematics"
print("Updated list after changing the 8th index to 'Mathematics':", schoolsubjects)

del schoolsubjects[3]
print("List after deleting the 4th index:", schoolsubjects)

sliced_subjects = schoolsubjects[2:6]
print("Sliced portion from index 2 to 5:", sliced_subjects)

print("Last index is", schoolsubjects[-1])