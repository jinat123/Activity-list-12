pokemonnames = [
    "Bulbasaur", "Charmander", "Squirtle", "Jigglypuff", "Meowth", "Psyduck", "Snorlax",
    "Eevee", "Mewtwo", "Gengar", "Machamp", "Lapras", "Vaporeon", "Jolteon", "Flareon"
]

print("Entire list:", pokemonnames)

print("9th index is", pokemonnames[9])

pokemonnames[11] = "Pikachu"
print("Updated list after changing the 12th index to 'Pikachu':", pokemonnames)

del pokemonnames[9]
print("List after deleting the 10th index:", pokemonnames)

sliced_pokemon = pokemonnames[4:8]
print("Sliced portion from index 4 to 7:", sliced_pokemon)

print("Last index is", pokemonnames[-1])