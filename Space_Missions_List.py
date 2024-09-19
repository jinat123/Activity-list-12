spacemissions = [
    "Voyager 1", "Hubble Space Telescope", "Curiosity Rover", "Cassini",
    "Apollo 13", "Pioneer 10", "Challenger", "International Space Station",
    "Mars Pathfinder", "New Horizons"
]

print("Entire list:", spacemissions)

print("7th index is", spacemissions[7])

spacemissions[3] = "Apollo 11"
print("Updated list after changing the 4th index to 'Apollo 11':", spacemissions)

del spacemissions[5]
print("List after deleting the 6th index:", spacemissions)

print("Last index is", spacemissions[-1])