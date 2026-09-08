class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def insert_end(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    def delete(self, song):
        if self.head is None:
            return
        if self.head.data == song:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.data == song:
                cur.next = cur.next.next
                return
            cur = cur.next

    def display(self):
        cur = self.head
        songs = []

        while cur is not None:
            songs.append(cur.data)
            cur = cur.next

        print("Playlist:", " -> ".join(songs) if songs else "Empty")

pl = Playlist()

pl.insert_end("Song1")
pl.insert_end("Song2")
pl.insert_end("Song3")
pl.insert_end("Song4")
pl.display()
pl.delete("Song2")
pl.display()
