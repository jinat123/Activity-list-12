studentnames = ["Alice", "Bob", "Charlie", "David", "Ella", "Frank", "Grace", "Hannah",
                 "Ivy", "Jack", "Kara", "Liam", "Mia", "Nathan", "Olivia", "Peter",
                 "Quincy", "Rachel", "Sam", "Tina"]

print("Entire list:", studentnames)

print("15th index is", studentnames[14])

studentnames[11] = "John"
print("Updated list after changing 12th index to 'John':", studentnames)

del studentnames[9]
print("List after deleting the 10th index:", studentnames)

sliced_portion = studentnames[2:6]
print("Sliced portion from index 2 to 5:", sliced_portion)

print("Last index is", studentnames[-1])