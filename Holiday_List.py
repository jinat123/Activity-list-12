holidays = [
    "New Year's Day", "Easter", "Thanksgiving", "Independence Day", "Halloween", "Labor Day",
    "Valentine's Day", "Memorial Day", "Diwali", "Hanukkah", "Boxing Day", "St. Patrick's Day"
]

print("Entire list:", holidays)

print("9th index is", holidays[9])

holidays[2] = "Christmas"
print("Updated list after changing the 3rd index to 'Christmas':", holidays)

del holidays[10]
print("List after deleting the 11th index:", holidays)

sliced_holidays = holidays[2:8]
print("Sliced portion from index 2 to 7:", sliced_holidays)

print("Last index is", holidays[-1])