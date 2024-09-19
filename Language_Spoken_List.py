languagesspoken = [
    "English", "Mandarin", "Hindi", "Arabic", "French", "Bengali", "Russian", "Portuguese",
    "Japanese", "German", "Korean", "Turkish", "Vietnamese", "Italian", "Thai", "Dutch",
    "Swahili", "Persian", "Urdu", "Tagalog"
]

print("Entire list:", languagesspoken)

print("13th index is", languagesspoken[13])

languagesspoken[9] = "Spanish"
print("Updated list after changing the 10th index to 'Spanish':", languagesspoken)

del languagesspoken[15]
print("List after deleting the 16th index:", languagesspoken)

sliced_languages = languagesspoken[6:12]
print("Sliced portion from index 6 to 11:", sliced_languages)

print("Last index is", languagesspoken[-1])