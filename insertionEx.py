# excercise insertion algorithm from scratch

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:   #
                currentNode = currentNode.next
            currentNode.next = newNode  # this is where the real thing happens

    def prepend(self, data):
        otherNode = Node(data)
        # otherNode = self.head
        otherNode.next = self.head
        self.head = otherNode

    def InsertLocationNode(self, location, data):
        NewNode = Node(data)
        # NewNode.next = prevNode.next
        # prevNode.next = NewNode
        temp = self.head
        # index = 1
        for index in range(1, location-1):
            temp = temp.next

        NewNode.next = temp.next
        temp.next = NewNode

    def deleteAnyNode(self, Index):
        if self.head is None:
            print('couldn\'t delete, the list doesn\'t exist ')
        else:
            num = 0
            tempNode = self.head  # its not working
            while num < Index:
                tempNode = tempNode.next
                num += 1
            tempNode = tempNode.next

    def deleteFirstNode(self):
        if self.head is None:
            print('couldn\'t delete, the list doesn\'t exist ')
        else:
            index = 0
            tempNode = self.head
            while index < 1:
                tempNode = tempNode.next
                index += 1
            self.head.next = tempNode.next
            self.head = tempNode

    def deleteLast(self):
        node = self.head
        while node.next:
            node = node.next
        node.next = None

    def show(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def searchForNode(self, data):
        node = self.head
        while node:
            if node.data == data:
                print(node.data)
            node = node.next


listed = linkedlist()
listed.add(12)
listed.add(3)
listed.add(5)
listed.InsertLocationNode(2, 'second One')

print("BEFORE DELETION")
listed.show()

# listed.deleteFirstNode()

print("AFTER DELETION")
# listed.deleteLast()
# listed.show()
listed.searchForNode('second One')
