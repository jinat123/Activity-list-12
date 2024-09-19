programminglanguages = [
    "Java", "C", "C++", "JavaScript", "Ruby", "Swift", "Kotlin", "Go", "R", "PHP",
    "Perl", "Rust", "TypeScript", "Scala"
]

print("Entire list:", programminglanguages)

print("11th index is", programminglanguages[11])

programminglanguages[8] = "Python"
print("Updated list after changing the 9th index to 'Python':", programminglanguages)

del programminglanguages[12]
print("List after deleting the 13th index:", programminglanguages)

sliced_languages = programminglanguages[5:12]
print("Sliced portion from index 5 to 12:", sliced_languages)

print("Last index is", programminglanguages[-1])