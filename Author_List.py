famousauthors = [
    "William Shakespeare", "Jane Austen", "Charles Dickens", "George Orwell", "J.K. Rowling",
    "Ernest Hemingway", "Leo Tolstoy", "F. Scott Fitzgerald", "Agatha Christie", "Virginia Woolf",
    "Gabriel Garcia Marquez", "Toni Morrison"
]

print("Entire list:", famousauthors)

print("6th index is", famousauthors[6])

famousauthors[3] = "Mark Twain"
print("Updated list after changing the 4th index to 'Mark Twain':", famousauthors)

del famousauthors[9]
print("List after deleting the 10th index:", famousauthors)

sliced_authors = famousauthors[3:9]
print("Sliced portion from index 3 to 8:", sliced_authors)

print("Last index is", famousauthors[-1])