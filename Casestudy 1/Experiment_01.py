stack = []

def book_return():
    book = input("Enter book name/id to return: ")
    stack.append(book)   

def book_arrange():
    if len(stack) == 0:
        print("Stack is empty. No book to arrange.")
    else:
        removed = stack.pop()  
        print("Arranged/Removed book:", removed)

def peek_top():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top book is:", stack[-1])

def display():
    print("Stack (bottom -> top):", stack)

while True:
    print("\n1 for Push(Return)\n2 for Pop(Arrange)\n3 for Top(Peek)\n4 for Display\n5 for Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_return()
    elif choice == 2:
        book_arrange()
    elif choice == 3:
        peek_top()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
