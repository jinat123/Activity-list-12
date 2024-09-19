famousrivers = [
    "Amazon River", "Yangtze River", "Mississippi River", "Ganges River", "Volga River",
    "Danube River", "Mekong River", "Thames River", "Rhine River", "Zambezi River"
]

print("Entire list:", famousrivers)

print("6th index is", famousrivers[6])

famousrivers[7] = "Nile River"
print("Updated list after changing the 8th index to 'Nile River':", famousrivers)

del famousrivers[8]
print("List after deleting the 9th index:", famousrivers)

print("Last index is", famousrivers[-1])