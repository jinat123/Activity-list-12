musicgenres = [
    "Rock", "Pop", "Hip-Hop", "Classical", "Electronic", "Reggae", "Country", "Blues", "Funk", "Disco",
    "Metal", "Soul", "Folk", "R&B", "Gospel"
]

print("Entire list:", musicgenres)

print("10th index is", musicgenres[10])

musicgenres[4] = "Jazz"
print("Updated list after changing the 5th index to 'Jazz':", musicgenres)

del musicgenres[6]
print("List after deleting the 7th index:", musicgenres)

sliced_genres = musicgenres[3:9]
print("Sliced portion from index 3 to 8:", sliced_genres)

print("Last index is", musicgenres[-1])