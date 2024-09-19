movietitles = [
    "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump", "The Shawshank Redemption",
    "Fight Club", "Interstellar", "Inglourious Basterds", "The Matrix", "The Lord of the Rings",
    "Gladiator", "Titanic", "Goodfellas", "Star Wars", "Avatar", "The Avengers", "Jurassic Park",
    "Braveheart", "The Lion King", "Schindler's List"
]

print("Entire list:", movietitles)

print("12th index is", movietitles[12])

movietitles[14] = "Inception"
print("Updated list after changing the 15th index to 'Inception':", movietitles)

del movietitles[17]
print("List after deleting the 18th index:", movietitles)

sliced_movies = movietitles[8:14]
print("Sliced portion from index 8 to 13:", sliced_movies)

print("Last index is", movietitles[-1])