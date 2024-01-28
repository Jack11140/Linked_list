from main import Node
from main import LinkedList

class StackUsingLinkedList(LinkedList):
    def push(self, data):
        self.prepend(data)

    def pop(self):
        if not self.is_empty():
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        else:
            return None

    def peek(self):
        return None if self.is_empty() else self.head.data

# 예제 사용
stack = StackUsingLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 출력: 3
print(stack.pop())  # 출력: 2
print(stack.peek())  # 출력: 1