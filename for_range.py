from main import Node

def linked_list_generator(start, end):
    current = start
    while current is not None:
        yield current.data
        current = current.next

def add(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def get(head, index):
    current = head
    for _ in range(index):
        if current is None:
            return None
        current = current.next
    return current.data

# 링크드 리스트 생성
head = Node(1)
head = add(head, 2)
head = add(head, 3)

# 제너레이터로 링크드 리스트 순회
linked_list_gen = linked_list_generator(head, None)
for data in linked_list_gen:
    print(data)

# get으로 데이터 가져오기
index_data = get(head, 1)
print("Data at index 1:", index_data)