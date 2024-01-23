#Linked list in Python
#Single linked list
#"If you lose self.head you lose it all :)"
class Node:
    """Tạo node class, mỗi node trong linked list sẽ
    là một đối tượng tạo từ Node, lưu ý, mỗi đối tượng sẽ có một address
    trong memory"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Linked_List:
    """Tạo một class linked list,
    mỗi đối tượng tạo từ class Linked_list này
    sẽ chứa các Node, lưu ý mỗi Linked_list object
    đều có thuộc tính head, nếu đối tượng rỗng, thì
    thuộc đính head này = None"""
    def __init__(self):
        """Mỗi đối tượng Linked_list được tạo sẽ
        có thuộc tính head ban đầu là None"""
        self.head = None
    def len(self):
        count = 1
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        return count
    def insert(self, data, index=0):
        """Giúp chèn một node vào trong linked_list"""
        #Nếu chưa có đối tượng nào trong linked_list:
        #Ta biến node đó thành head
        if self.head is None:
            node = Node(data)#Lúc này node vừa là head vừa là last node!
            self.head = node
        else:
            if index >= self.len():
                current = self.head
                while current.next:
                    current = current.next
                current.next = Node(data)
                return

            position = 2#first node is 1, now current points to the second node
            current = self.head
            new_node = Node(data, current)

            while position <= index:
                position += 1
                if current.next:
                    current = current.next

            new_node.next = current.next
            current.next = new_node

    def print(self):
        """Để in ra các nodes có trong linked list"""
        itr = self.head
        result = ""
        while itr:
            """Nếu một node không phải là last node, tức nó không phải là None, vòng lặp while sẽ tiếp tục chạy"""
            result += str(itr.data) + "-->"
            itr = itr.next#itr.next "chứa" một đối tượng node khác hoặc None nếu là last node
        print(result)


if __name__ == "__main__":
    fruit_list = Linked_List()#Lúc này fruit_list.head = None
    fruit_list.insert("Bananas")
    fruit_list.insert("Tomato",1)
    fruit_list.insert("Straw berries", 1)
    fruit_list.insert("Water melon", 1)
    fruit_list.insert("Lemon", 2)
    fruit_list.insert("Jackfruit", 1)
    fruit_list.insert("Straw berries222222222", 11)
    fruit_list.print()
    a = fruit_list.len()
    print(a)
