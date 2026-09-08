MAX = 75
q = []                 
borrowed = set()      
in_queue = set()      


def mark_borrowed():
    book_id = input("Book ID (mark as borrowed): ").strip()
    borrowed.add(book_id)
    print("Done")


def enqueue_return():
    if len(q) == MAX:
        print("Queue is full!")
        return

    book_id = input("Book ID to return: ").strip()

    if book_id not in borrowed:
        print("This book was not borrowed!")
        return

    if book_id in in_queue:
        print("Duplicate in queue!")
        return

    q.append(book_id)
    in_queue.add(book_id)
    borrowed.remove(book_id)
    print("Added to return queue")


def dequeue_process():
    if len(q) == 0:
        print("Queue is empty!")
        return

    first_id = q.pop(0)        
    in_queue.remove(first_id)
    print("Processed:", first_id)


def next_order():
    if not q:
        print("Queue is empty!")
        return

    order = q
    print(q)

def display_queue():
    print("Queue:", q)


while True:
    print("\n1 Mark borrowed")
    print("2 Return book (enqueue)")
    print("3 Process return (dequeue)")
    print("4 View next (peek)")
    print("5 Display queue")
    print("6 Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        mark_borrowed()
    elif ch == 2:
        enqueue_return()
    elif ch == 3:
        dequeue_process()
    elif ch == 4:
        next_order()
    elif ch == 5:
        display_queue()
    elif ch == 6:
        break
    else:
        print("Wrong choice")
