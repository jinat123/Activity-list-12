carpentrytools = [
    "Saw", "Chisel", "Plane", "Drill", "Tape Measure", "Level", "Screwdriver",
    "Clamps", "Square", "Mallet"
]

print("Entire list:", carpentrytools)

print("4th index is", carpentrytools[4])

carpentrytools[6] = "Hammer"
print("Updated list after changing the 7th index to 'Hammer':", carpentrytools)

del carpentrytools[4]
print("List after deleting the 5th index:", carpentrytools)

print("Last index is", carpentrytools[-1])