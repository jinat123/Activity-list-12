videogametitles = [
    "The Legend of Zelda", "Super Mario Bros", "Halo", "Fortnite", "Call of Duty",
    "League of Legends", "Overwatch", "Grand Theft Auto V", "The Witcher 3", "Red Dead Redemption",
    "Animal Crossing", "Cyberpunk 2077", "Dark Souls", "Assassin's Creed", "Final Fantasy"
]

print("Entire list:", videogametitles)

print("7th index is", videogametitles[7])

videogametitles[3] = "Minecraft"
print("Updated list after changing the 4th index to 'Minecraft':", videogametitles)

del videogametitles[8]
print("List after deleting the 9th index:", videogametitles)

sliced_games = videogametitles[5:11]
print("Sliced portion from index 5 to 10:", sliced_games)

print("Last index is", videogametitles[-1])