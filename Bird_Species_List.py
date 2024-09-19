birdspecies = [
    "Sparrow", "Parrot", "Penguin", "Owl", "Flamingo", "Peacock",
    "Hummingbird", "Woodpecker", "Crow", "Dove", "Swan", "Kingfisher"
]

print("Entire list:", birdspecies)

print("9th index is", birdspecies[9])

birdspecies[5] = "Eagle"
print("Updated list after changing the 6th index to 'Eagle':", birdspecies)

del birdspecies[7]
print("List after deleting the 8th index:", birdspecies)

sliced_birds = birdspecies[3:8]
print("Sliced portion from index 3 to 7:", sliced_birds)

print("Last index is", birdspecies[-1])