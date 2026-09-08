queue = ["C101", "C102", "C103", "C104"]

# Display the queue
print("Initial Queue:", queue)

# Delete Customer C101
if "C101" in queue:
    queue.remove("C101")
    print("Deleted C101")
else:
    print("C101 not found")

# Insert Customer C105 (at end)
queue.append("C105")
print("Inserted C105")

# Display the final queue
print("Final Queue:", queue)
