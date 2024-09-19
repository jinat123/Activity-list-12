landanimalsspeeds = [
    "Elephant - 40 km/h", "Horse - 88 km/h", "Kangaroo - 71 km/h", "Lion - 80 km/h",
    "Giraffe - 60 km/h", "Greyhound - 72 km/h", "Cheetah - 100 km/h",
    "Zebra - 65 km/h", "Leopard - 58 km/h", "Ostrich - 70 km/h",
    "Hyena - 60 km/h", "Tiger - 65 km/h"
]

print("Entire list:", landanimalsspeeds)

print("7th index is", landanimalsspeeds[7])

landanimalsspeeds[8] = "Cheetah - 120 km/h"
print("Updated list after changing the 9th index to 'Cheetah - 120 km/h':", landanimalsspeeds)

del landanimalsspeeds[9]
print("List after deleting the 10th index:", landanimalsspeeds)

sliced_animals = landanimalsspeeds[3:8]
print("Sliced portion from index 3 to 7:", sliced_animals)

print("Last index is", landanimalsspeeds[-1])