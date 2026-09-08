stack = []
MAX_BOXES = 40

def store_box():
    if len(stack) >= MAX_BOXES:
        print("Stack full! Cannot store more.")
        return

    box_id = input("Box ID: ").strip()

    for b in stack:
        if b["id"] == box_id:
            print("This Box ID already exists!")
            return

    weight = float(input("Weight (kg): "))

    if weight < 1 or weight > 50:
        print("Invalid weight! Must be between 1 and 50 kg.")
        return

    fragile = input("Fragile? (yes/no): ").strip().lower()
    is_fragile = (fragile == "yes")

    if is_fragile and weight > 20:
        print("Fragile box over 20 kg cannot be stored.")
        return

    stack.append({"id": box_id, "weight": weight, "fragile": is_fragile})
    print("Box stored!")

def remove_box():
    if len(stack) == 0:
        print("No boxes to remove.")
    else:
        removed = stack.pop()
        print("Removed box:", removed["id"])

def top_box():
    if len(stack) == 0:
        print("Box stack is empty.")
    else:
        top = stack[-1]
        print("Top box:", top["id"])

def display_stack():
    if len(stack) == 0:
        print("Box stack is empty.")
    else:
        print("Box Stack (bottom -> top):")
        print(stack)

while True:
    print("\n1 Store Box (Push)")
    print("2 Remove Box (Pop)")
    print("3 Top Box (Peek)")
    print("4 Display Box Stack")
    print("5 Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        store_box()
    elif ch == 2:
        remove_box()
    elif ch == 3:
        top_box()
    elif ch == 4:
        display_stack()
    elif ch == 5:
        break
    else:
        print("Invalid choice!")
