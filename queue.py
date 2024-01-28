from main import Node
from main import LinkedList


class QueueUsingLinkedList(LinkedList):
    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            dequeued_data = self.head.data
            self.head = self.head.next
            return dequeued_data
        else:
            return None

    def peek(self):
        return None if self.is_empty() else self.head.data

# 예제 사용
queue = QueueUsingLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # 출력: 1
print(queue.dequeue())  # 출력: 2
print(queue.peek())  # 출력: 3