festivals = [
    "Carnival", "Oktoberfest", "Holi", "Chinese New Year", "Mardi Gras", "Rio Carnival",
    "Day of the Dead", "La Tomatina", "Diwali", "Eid al-Fitr", "Thanksgiving", "Christmas",
    "St. Patrick's Day", "Hanami", "Songkran"
]

print("Entire list:", festivals)

print("7th index is", festivals[7])

festivals[10] = "Diwali"
print("Updated list after changing the 11th index to 'Diwali':", festivals)

del festivals[8]
print("List after deleting the 9th index:", festivals)

sliced_festivals = festivals[5:13]
print("Sliced portion from index 5 to 12:", sliced_festivals)

print("Last index is", festivals[-1])