queue = []

def enqueue():
    name = input("Enter name for ticket: ")
    queue.append(name)   # insert at end
    print("Added to queue")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        removed = queue.pop(0)  # remove from front
        print("Removed:", removed)

def display():
    print("Queue:", queue)

while True:
    print("\n1 Enqueue\n2 Dequeue\n3 Display\n4 Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Wrong choice!")
