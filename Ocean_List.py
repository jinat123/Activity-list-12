oceans = [
    "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean", "Pacific Ocean"
]

print("Entire list:", oceans)

print("3rd index is", oceans[3])

oceans[1] = "Pacific Ocean"
print("Updated list after changing the 2nd index to 'Pacific Ocean':", oceans)

del oceans[3]
print("List after deleting the 4th index:", oceans)

print("Last index is", oceans[-1])