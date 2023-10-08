class Node:
    def __init__(self, value):
        self.key = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addLast(self, k):
        newNode = Node(k)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                if temp.key == k:
                    return
                temp = temp.next
            if temp.key == k:
                return
            temp.next = newNode

    def addFirst(self, k):
        newNode = Node(k)
        temp = self.head

        while temp:
            if temp.key == k:
                return
            temp = temp.next

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAfter(self, u, v):
        newNode = Node(u)
        temp = self.head

        while temp:
            if temp.key == u:
                return
            temp = temp.next

        temp = self.head
        while temp is not None:
            if temp.key == v:
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next

    def addBefore(self, u, v):
        if self.head.key == v:
            self.addFirst(u)

        newNode = Node(u)
        temp = self.head

        while temp:
            if temp.key == u:
                return
            temp = temp.next

        temp = self.head
        while temp.next is not None:
            if temp.next.key == v:
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next

    def reversed(self):
        prev = None
        temp = self.head

        while temp:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode

        self.head = prev

    def remove(self, k):
        temp = self.head

        # Special case: If the node to remove is the head node
        if temp and temp.key == k:
            self.head = temp.next
            return

        # Search for the node to remove and keep track of the previous node
        prev = None
        while temp and temp.key != k:
            prev = temp
            temp = temp.next

        # If the node is found, update the previous node's next reference
        # to skip the node to remove
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.key, end=' ')
            temp = temp.next
        print('')


if __name__ == "__main__":
    linked_list = LinkedList()
    n = int(input())
    k = input().split()
    for each in k:
        linked_list.addLast(int(each))
    while True:
        command = input().split()
        if command[0] == "addlast":
            linked_list.addLast(int(command[1]))
        elif command[0] == "addfirst":
            linked_list.addFirst(int(command[1]))
        elif command[0] == "addafter":
            linked_list.addAfter(int(command[1]), int(command[2]))
        elif command[0] == "addbefore":
            linked_list.addBefore(int(command[1]), int(command[2]))
        elif command[0] == "reverse":
            linked_list.reversed()
        elif command[0] == "remove":
            linked_list.remove(int(command[1]))
        elif command[0] == "#":
            break
        else:
            continue

    linked_list.display()
