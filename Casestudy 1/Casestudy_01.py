stack = []
MAX = 25

def push_action():
    t = input("Insert/Delete/Replace: ").strip()
    if t not in ["Insert", "Delete", "Replace"]:
        print("Invalid action, ignored.")
        return

    d = input("Enter details: ").strip()
    action = (t, d)

    if len(stack) > 0 and stack[-1] == action:
        print("Duplicate action, not stored.")
        return

    if len(stack) >= MAX:
        print("Stack full (max 25). Ignored.")
        return

    stack.append(action)
    print("Action pushed.")

def pop_undo():
    if len(stack) == 0:
        print("Nothing to undo.")
    else:
        a = stack.pop()
        print("Undid:", a)

def peek_last():
    if len(stack) == 0:
        print("No actions.")
    else:
        print("Last action:", stack[-1])

def display_stack():
    print("Action Stack:", stack)

while True:
    print("\n1 Push(Perform)\n2 Pop(Undo)\n3 Peek(Last)\n4 Display\n5 Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        push_action()
    elif ch == 2:
        pop_undo()
    elif ch == 3:
        peek_last()
    elif ch == 4:
        display_stack()
    elif ch == 5:
        break
    else:
        print("Invalid choice.")
