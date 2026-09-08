MAX = 60
q = []                 
valid_tokens = set()  
in_queue = set()       

def add_valid_token():
    t = input("Enter valid token number: ").strip()
    valid_tokens.add(t)
    print("Token saved")

def enqueue_customer():
    if len(q) == MAX:
        print("Queue overflow! (Full)")
        return

    token = input("Enter token number to join queue: ").strip()

    if token not in valid_tokens:
        print("Invalid token! Not allowed")
        return

    if token in in_queue:
        print("Duplicate token! Already in queue")
        return

    q.append(token)
    in_queue.add(token)
    print("Customer added")

def dequeue_customer():
    if len(q) == 0:
        print("Queue is empty! (No customer)")
        return

    first = q.pop(0)       # remove from front
    in_queue.remove(first)
    print("Served customer token:", first)

def next_customer():
    if len(q) == 0:
        print("Queue is empty! (No next)")
        return

    print("Next customer token:", q)

def display_queue():
    print("Customer Queue:", q)

while True:
    print("\n1 Add valid token")
    print("2 Add customer to queue (Enqueue)")
    print("3 Serve customer (Dequeue)")
    print("4 View next customer")
    print("5 Display queue")
    print("6 Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        add_valid_token()
    elif ch == 2:
        enqueue_customer()
    elif ch == 3:
        dequeue_customer()
    elif ch == 4:
        next_customer()
    elif ch == 5:
        display_queue()
    elif ch == 6:
        break
    else:
        print("Wrong choice")
