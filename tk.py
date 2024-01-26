import tkinter as tk

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
        else:
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

#GUI 구현-인스턴스 개념과 tk메소드들을 이용하여 링크드리스트를 gui에서 사용하기

class LinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("링크드 리스트")

        self.linked_list = LinkedList()
        self.create_ui()

    def create_ui(self):
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        
        add_button = tk.Button(self.master, text="노드 추가", command=self.add_node)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        prepend_button = tk.Button(self.master, text="노드 앞에 추가", command=self.prepend_node)
        prepend_button.grid(row=0, column=2, padx=10, pady=10)

        delete_button = tk.Button(self.master, text="노드 삭제", command=self.delete_node)
        delete_button.grid(row=0, column=3, padx=10, pady=10)

        display_button = tk.Button(self.master, text="리스트 출력", command=self.display_list)
        display_button.grid(row=1, column=0, columnspan=4, pady=10)

        self.label = tk.Label(self.master, text="")
        self.label.grid(row=2, column=0, columnspan=4, pady=10)

    def add_node(self):
        data = self.entry.get()
        if data.isdigit():
            self.linked_list.append(int(data))
            self.entry.delete(0, tk.END)
            print(f"데이터가 {data}인 노드를 추가했습니다.")
        else:
            print("유효하지 않은 입력입니다. 정수를 입력하세요.")

    def prepend_node(self):
        data = self.entry.get()
        if data.isdigit():
            self.linked_list.prepend(int(data))
            self.entry.delete(0, tk.END)
            print(f"데이터가 {data}인 노드를 맨 앞에 추가했습니다.")
        else:
            print("유효하지 않은 입력입니다. 정수를 입력하세요.")

    def delete_node(self):
        data = self.entry.get()
        if data.isdigit():
            self.linked_list.delete(int(data))
            self.entry.delete(0, tk.END)
            print(f"데이터가 {data}인 노드를 삭제했습니다.")
        else:
            print("유효하지 않은 입력입니다. 정수를 입력하세요.")

    def display_list(self):
        display_text = "링크드 리스트: "
        current_node = self.linked_list.head
        while current_node:
            display_text += str(current_node.data) + " -> "
            current_node = current_node.next
        display_text += "None"
        self.label.config(text=display_text)

def main():
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()

##print_list - 콘솔 출력, display_list - GUI 출력

# main GUI 실행
if __name__ == "__main__":
    main()

# LinkedList 콘솔 테스트
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.delete(2)

my_linked_list.print_list()  # 출력: 1 -> 3 -> None