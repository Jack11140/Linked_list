import tkinter as tk

from main import Node
from main import LinkedList

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