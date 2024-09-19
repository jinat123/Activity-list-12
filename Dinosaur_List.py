dinosaurnames = [
    "Triceratops", "Stegosaurus", "Velociraptor", "Brachiosaurus", "Allosaurus", "Ankylosaurus", "Spinosaurus", "Diplodocus"
]

print("Entire list:", dinosaurnames)

print("4th index is", dinosaurnames[4])

dinosaurnames[5] = "Tyrannosaurus Rex"
print("Updated list after changing the 6th index to 'Tyrannosaurus Rex':", dinosaurnames)

del dinosaurnames[6]
print("List after deleting the 7th index:", dinosaurnames)

print("Last index is", dinosaurnames[-1])