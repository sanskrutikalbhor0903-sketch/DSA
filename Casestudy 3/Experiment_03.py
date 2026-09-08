class Node:
    def __init__(self, book_id):
        self.data = book_id
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, book_id):
        new_node = Node(book_id)
        new_node.next = self.head
        self.head = new_node
        print("Inserted at beginning")

    # Insert at end
    def insert_at_end(self, book_id):
        new_node = Node(book_id)

        if self.head is None:
            self.head = new_node
            print("Inserted at end (first node)")
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node
        print("Inserted at end")

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty!")
            return

        self.head = self.head.next
        print("Deleted from beginning")

    # Display
    def display(self):
        if self.head is None:
            print("List is empty!")
            return

        cur = self.head
        print("List:", end=" ")
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

lst = SinglyLinkedList()

while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete from beginning")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter book ID: "))
        lst.insert_at_beginning(x)

    elif ch == 2:
        x = int(input("Enter book ID: "))
        lst.insert_at_end(x)

    elif ch == 3:
        lst.delete_from_beginning()

    elif ch == 4:
        lst.display()

    elif ch == 5:
        break

    else:
        print("Wrong choice")
