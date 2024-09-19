naturallandmarks = [
    "Mount Everest", "Niagara Falls", "Great Barrier Reef", "Victoria Falls",
    "Amazon Rainforest", "Sahara Desert", "Yosemite Valley", "Mount Fuji",
    "Angel Falls", "Galapagos Islands"
]

print("Entire list:", naturallandmarks)

print("8th index is", naturallandmarks[8])

naturallandmarks[4] = "Grand Canyon"
print("Updated list after changing the 5th index to 'Grand Canyon':", naturallandmarks)

del naturallandmarks[8]
print("List after deleting the 9th index:", naturallandmarks)

print("Last index is", naturallandmarks[-1])