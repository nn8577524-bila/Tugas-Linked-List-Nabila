class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_before(self, data, value):
        if self.is_empty():
            return
        current = self.head
        while current:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current
                current.previous.next = new_node
                new_node.previous = current.previous
                current.previous = new_node
                return
            else:
                current = current.next

    def insert_after(self, data, value):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            current = self.head
            while current:
                if current.data == value:
                    new_node.next = current.next
                    current.next.previous = new_node
                    new_node.previous = current
                    current.next = new_node
                    return
                else:
                    current = current.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_beginning(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return data

    def delete_at_middle(self, data):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return
                else:
                    current = current.next

    def delete_from_end(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.previous
        print()

# Example usage
dll = DoubleLinkedList()
print('Tambah Data 5, 10 di bagian depan')
dll.insert_at_beginning(5)
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
print('\nMenampilkan data dari depan ke belakang : ', end=' ')
dll.display_forward()  # Output: 30 20 10 5
print('\nMenampilkan data dari belakang ke depan : ', end=' ')
dll.display_backward()  # Output: 5 10 20 30

print('\nMenambahkan simpul 25 sebelum simpul 20')
dll.insert_before(25, 20)
dll.display_forward()  # Output: 30 25 20 10 5
print('\nMenambahkan simpul 17 setelah simpul 10')
dll.insert_after(17, 10)
dll.display_forward()  # Output: 30 25 20 10 17 5

print('\nMenghapus data di bagian depan')
dll.delete_from_beginning()
dll.display_forward()  # Output: 25 20 10 17 5

print('\nMenghapus data di bagian akhir')
dll.delete_from_end()
dll.display_forward()  # Output: 25 20 10 17

print('\nDelete simpul 20')
dll.delete_at_middle(20)
dll.display_forward()  # Output: 25 10 17

print('\nData linked list setelah delete data: ', end=' ')
dll.display_forward()  # Output: 10 17 25
