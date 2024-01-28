class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is not None:
            return current.data
        else:
            raise IndexError("Index out of range")

    #iter()함수 사용을 위한, 즉 순회를 위해
    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data
        else:
            raise StopIteration
            # 반복이 끝났음을 나타내기 위해 StopIteration 예외 대신 None 반환
            # return None

# LinkedList 콘솔 테스트
if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.delete(2)
    my_linked_list.print_list()  # 출력: 1 -> 3 -> None